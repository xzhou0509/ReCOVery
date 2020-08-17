import numpy as np
import os
from cnn import *
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'
from sklearn.model_selection import train_test_split
# import xlwt
import tensorflow as tf
import json


#  Hyperparameters
tf.compat.v1.flags.DEFINE_integer("head_size", 30, "the length of headline matrix")


tf.compat.v1.flags.DEFINE_float("num_filters", 16, "the number of filters)")
tf.compat.v1.flags.DEFINE_float("final_len", 16, "the output length of fully connected layer)")

# Training parameters
tf.compat.v1.flags.DEFINE_integer("batch_size", 8, "Batch Size (Default: 64)")
tf.compat.v1.flags.DEFINE_integer("num_epochs", 2000, "Number of training epochs (Default: 100)")
tf.compat.v1.flags.DEFINE_integer("num_batchs", 16, "Number of batchs per fold (Default: 100)")
tf.compat.v1.flags.DEFINE_float("l2_reg_lambda", 3.0, "L2 regularization lambda (Default: 3.0)")
tf.compat.v1.flags.DEFINE_float("learning_rate", 1e-4, "Which learning rate to start with.")
tf.compat.v1.flags.DEFINE_float("dropout_keep_prob", 0.5, "Dropout keep probability (Default: 0.5)")

# Misc Parameters
tf.compat.v1.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.compat.v1.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")


FLAGS = tf.compat.v1.flags.FLAGS
FLAGS.flag_values_dict()
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
    print("{} = {}".format(attr.upper(), value._value))


def train(x_train_head, y_train, modelfolder, boarddir):

    with tf.Graph().as_default():
        session_conf = tf.compat.v1.ConfigProto(
            allow_soft_placement=FLAGS.allow_soft_placement,
            log_device_placement=FLAGS.log_device_placement)
        sess = tf.compat.v1.Session(config=session_conf)

        with sess.as_default():
            layer = Graph(head_size=FLAGS.head_size,
                          input_len=32,
                          embedding_len=300,
                          l2_reg_lambda=FLAGS.l2_reg_lambda,
                          lr=FLAGS.learning_rate,
                          num_filters=FLAGS.num_filters,
                          final_len=FLAGS.final_len)

            # Initialize all variables
            sess.run(tf.compat.v1.global_variables_initializer())
            writer1 = tf.compat.v1.summary.FileWriter(boarddir, sess.graph)

            print("Train...\n")
            length = int(float(len(y_train)) / 5)

            for epoch in range(FLAGS.num_epochs):
                print(' ----------- epoch No.' + str(epoch + 1) + ' ----------- ')
                for i in range(5):  # 5-fold
                    print('fold No.', str(i + 1))
                    x_dev_head = x_train_head[i * length: (i + 1) * length]
                    x_t_head = np.concatenate((x_train_head[:i * length], x_train_head[(i + 1) * length:]), axis=0)

                    y_dev = y_train[i * length: (i + 1) * length]
                    y_t = np.concatenate((y_train[:i * length], y_train[(i + 1) * length:]), axis=0)

                    for batch in range(FLAGS.num_batchs):

                        batch_indices = np.random.choice(np.arange(y_t.shape[0]), FLAGS.batch_size)
                        x_batch_head = x_t_head[batch_indices]
                        y_batch = y_t[batch_indices]

                        _, train_accuracy, trainloss = \
                            sess.run([layer.train_op, layer.accuracy, layer.loss], feed_dict={layer.input_headline__: x_batch_head,
                                                                                              layer.input_y_: y_batch,
                                                                                              layer.dropout_keep_prob: FLAGS.dropout_keep_prob,
                                                                                              layer.batch_size: FLAGS.batch_size})

                        if (batch + 1) % 50 == 0:
                            print(" step %d, training accuracy: %g,  loss %g" % ((batch + 1), train_accuracy, trainloss))

                    # training set
                    summary1 = sess.run(layer.merged, feed_dict={layer.input_headline__: x_batch_head,
                                                                 layer.input_y_: y_batch,
                                                                 layer.dropout_keep_prob: FLAGS.dropout_keep_prob,
                                                                 layer.batch_size: FLAGS.batch_size})


                    # draw training set
                    writer1.add_summary(summary1, epoch * 5 + i)

                    # validation set
                    dev_accuracy_fake, dev_loss = sess.run(
                        [layer.accuracy, layer.loss], feed_dict={layer.input_headline__: x_dev_head,
                                                                               layer.input_y_: y_dev,
                                                                               layer.dropout_keep_prob: 1.0,
                                                                               layer.batch_size: len(y_dev)})

                    print("validation accuracy:%g, loss: %g" % (dev_accuracy_fake, dev_loss))

                if (epoch + 1) % 10 == 0:
                    saver = tf.compat.v1.train.Saver()
                    saver.save(sess, modelfolder + str(epoch+1))




def main(_):
    print('===============================================')
    print('load vectors and labels ... ')

    with open('～/text-cnn/dic_embedding.json', 'r') as f:
        dic = json.load(f)

    x_head = []
    y = []
    for key, value in dic.items():
        tmp = []
        tmp = [float(i) for j in value['title'] for i in j]
        tmp = np.array(tmp).reshape((-1, 300))
        x_head.append(tmp)


        if value['reliability'] == '1':
            y.append([1, 0])
        else:
            y.append([0, 1])

    x_head = np.array(x_head)
    y = np.array(y)
   

    print('split training set and test set ... ')
    x_head_train, x_head_test, y_train, y_test = train_test_split(x_head, y, test_size=0.2, random_state=4)
    
    modelfolder = '～/text-cnn/ckp/'
    if not os.path.exists(modelfolder):
        os.makedirs(modelfolder)
    log = '～/text-cnn/runs/logs/'
    if not os.path.exists(log):
        os.makedirs(log)

    train(x_head_train, y_train, modelfolder, log)


if __name__ == '__main__':
    tf.compat.v1.app.run()