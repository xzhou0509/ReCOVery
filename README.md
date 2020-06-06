

## ReCOVery

***The latest dataset paper with detailed analysis on the dataset can be found at [Add link]***

This is the first version of the dataset and will be updated timely.

## Overview  

The complete dataset cannot be distributed because of Twitter privacy policies and news publisher copy rights.  Social engagements and user information are not disclosed because of Twitter Policy. The code in this repository can be used to download news articles from published websites and relevant social media data from Twitter. 

The repository contains 4 folders namely - code, dataset, features and figure

The dataset provided in this repository (located in `dataset` folder) include following files:

 - `recovery-news-data.csv` -  Samples of all news articles collected from 21 reliable and 38 unreliable websites 
 - `recovery-social-media-data.csv` -  Samples of social media information of news articles from above websites

Each of the above CSV files is comma separated file and have the following respective columns:

1. recovery-news-data.csv
 - `news_id` - Unique identifider for each news article.
 - `url` - Url of the article from web that published that news. 
 - `publisher` - Publisher of the news article.
 - `author` - Author or authors of the article. This field is a list of names of authors separated by command.
 - `title` - Tweet ids of tweets sharing the news. This field is list of tweet ids separated by tab.
 - `image` - Head image of the news article.
 - `body_text` - The full body content of the news article.
 - `news_guard_score` - The score given by NewsGuard for the news source.
 - `mbfc_level` - Media Bias/Fact Check level for each news source.
 - `political_bias` - Political bias for each news source
 - `country` - Tweet ids of tweets sharing the news. This field is list of tweet ids separated by tab.
 - `reliability` - Tweet ids of tweets sharing the news. This field is list of tweet ids separated by tab.
 


## Installation    

###  Requirements:
## TODO: ADD

 Data download scripts are writtern in python and requires `python 3.6 +` to run.
 
Twitter API keys are used for collecting data from Twitter.  Make use of the following link to get Twitter API keys    
https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html   

Script make use of keys from  _tweet_keys_file.json_ file located in `code/resources` folder. So the API keys needs to be updated in `tweet_keys_file.json` file.  Provide the keys as array of JSON object with attributes `app_key,app_secret,oauth_token,oauth_token_secret` as mentioned in sample file.

Install all the libraries in `requirements.txt` using the following command
    
    pip install -r requirements.txt


###  Configuration:

## TODO: ADD

## Running Code
# TODO: List files to execute


### Dataset Structure
The downloaded dataset will have the following  folder structure,
```bash
├── code
│   ├── news_articles
│   │   ├── recovery-news-data.csv
│   │	
│   └── social_media
│      ├── gossipcop-1
│      │	
│      │	
│      │	
│		└── ....		
├── dataset
│   ├── news_articles
│   │   ├── recovery-news-data.csv
│   │   │	
│   │   │	
│   │   │	
│   │		
│   │
│   └── real
│      ├── poliifact-2
│      │	├── news content.json
│      │	├── tweets
│      │	└── retweets
│      └── ....					
├── feature
│		├── 374136824.json
│		├── 937649414600101889.json
│   		└── ....
├── figure
│		├── 374136824.json
│		├── 937649414600101889.json
│	   	└── ....
└── user_followers
│		├── 374136824.json
│		├── 937649414600101889.json
│	   	└── ....
└──user_following
        	├── 374136824.json
		├── 937649414600101889.json
	   	└── ....
```
**News Content**

`news content.json`:
This json includes all the meta information of the news articles collected using the provided news source URLs. This is a JSON object with attributes including:

 - `text` is the text of the body of the news article. 
 - `images` is a list of the URLs of all the images in the news article web page. 
 - `publish date`  indicate the date that news article is published.

**Social Context**

**`tweets` folder**:
This folder contains all tweets related to the news sample. This contains the tweet objects of the all the tweet ids provided in the tweet_ids attribute of the dataset csv. All the files in this folder are named as `<tweet_id>.json` . Each `<tweet_id>.json` file is a JSON file with format mentioned in [https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html).

**`retweets` folder**:
This folder contains the retweets of the all tweets posted sharing a particular news article. This folder contains files named as  `<tweet_id>.json` and it contains a array of the retweets for a particular tweets.  Each object int the retweet array have format mentioned in [https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-retweets-id](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-retweets-id).

**`user_profiles` folder**:
This folder contains all the user profiles of the users posting tweets related to all news articles. This same folder is used for both datasources ( Politifact and GossipCop). It contains files named as `<user_id>.json` and have JSON formated mentioned in [https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object.html](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object.html)

**`user_timeline_tweets` folder**:
This folder contains files representing the time line of tweets of users posting tweets related to fake and real news. All files in the folder are named as `<user_id>.json` and have JSON array of upto 200 recent tweets of the users. The files have format mentioned same as [https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html).

**`user_followers` folder**:
This folder contains all the user followers ids of the users posting tweets related to all news articles. This same folder is used for both datasources ( Politifact and GossipCop). It contains files named as `<user_id>.json` and have JSON data with `user_id` and `followers` attributes.

**`user_following` folder**:
This folder contains all the user following ids of the users posting tweets related to all news articles. This same folder is used for both datasources ( Politifact and GossipCop). It contains files named as `<user_id>.json` and have JSON data with `user_id` and `following` attributes.


## References
If you use this dataset, please cite the following papers:
~~~~
@article{shu2018fakenewsnet,
  title={FakeNewsNet: A Data Repository with News Content, Social Context and Dynamic Information for Studying Fake News on Social Media},
  author={Shu, Kai and  Mahudeswaran, Deepak and Wang, Suhang and Lee, Dongwon and Liu, Huan},
  journal={arXiv preprint arXiv:1809.01286},
  year={2018}
}
~~~~
~~~~
@article{shu2017fake,
  title={Fake News Detection on Social Media: A Data Mining Perspective},
  author={Shu, Kai and Sliva, Amy and Wang, Suhang and Tang, Jiliang and Liu, Huan},
  journal={ACM SIGKDD Explorations Newsletter},
  volume={19},
  number={1},
  pages={22--36},
  year={2017},
  publisher={ACM}
}
~~~~
~~~~
@article{shu2017exploiting,
  title={Exploiting Tri-Relationship for Fake News Detection},
  author={Shu, Kai and Wang, Suhang and Liu, Huan},
  journal={arXiv preprint arXiv:1712.07709},
  year={2017}
}
~~~~



[Fake News Detection on Social Media: A Data Mining Perspective]:<https://arxiv.org/abs/1708.01967>
[Exploiting Tri-Relationship for Fake News Detection]:<http://arxiv.org/abs/1712.07709>
[FakeNewsTracker]:<http://blogtrackers.fulton.asu.edu:3000>
[FakeNewsNet]:<https://arxiv.org/abs/1809.01286>

(C) 2019 Arizona Board of Regents on Behalf of ASU


