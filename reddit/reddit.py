import config  # Assuming you have a 'config.py' file with your Reddit credentials
import requests, pandas as pd, praw


def connect_reddit():
     return praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_SECRET_KEY,
        user_agent='RedditReader/0.0.1',
        username= config.REDDIT_USERNAME,
        password=config.REDDIT_PASSWORD
    )

def get_post(headers, url):
    res = requests.get(f"{url}.json", headers=headers)
    print(f"{url}.json")
    print(res)

def new_get_host_posts(reddit, subreddit_name, no_of_posts):
    return reddit.subreddit(subreddit_name).hot(limit=no_of_posts)


def get_hot_posts(headers):
    # List to store data of posts
    post_data = []

    # Make a request for the trending posts in /r/Python
    res = requests.get("https://oauth.reddit.com/r/TrueOffMyChest/hot",
                    headers=headers,
                    params={'limit':'100'})

    # Loop through each post received from GET reqeust
    for post in res.json()['data']['children']:
            # append relevant data to dataframe
            post_data.append({
            'subreddit': post['data']['subreddit'],
            'title': post['data']['title'],
            'selftext': post['data']['selftext'],
            'upvote_ratio': post['data']['upvote_ratio'],
            'ups': post['data']['ups'],
            'downs': post['data']['downs'],
            'score': post['data']['score']
            })
            
    return pd.DataFrame(post_data)