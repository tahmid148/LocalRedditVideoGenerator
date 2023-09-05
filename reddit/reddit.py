import config  # Assuming you have a 'config.py' file with your Reddit credentials
import requests, praw

def connect_reddit():
     return praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_SECRET_KEY,
        user_agent='RedditReader/0.0.1',
        username= config.REDDIT_USERNAME,
        password=config.REDDIT_PASSWORD
    )

def get_post(reddit, id):
    return reddit.submission(id)
    

def get_hot_posts(reddit, subreddit_name, no_of_posts):
    return reddit.subreddit(subreddit_name).hot(limit=no_of_posts)