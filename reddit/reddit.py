import config  # Assuming you have a 'config.py' file with your Reddit credentials
import requests, pandas as pd

def connect_reddit():
    # Set up basic authentication using client ID and secret key
    auth = requests.auth.HTTPBasicAuth(config.REDDIT_CLIENT_ID, config.REDDIT_SECRET_KEY)

    # Define the data for the authentication request
    data = {
        'grant_type': 'password',
        'username': config.REDDIT_USERNAME,
        'password': config.REDDIT_PASSWORD
    }

    # Set custom user-agent in headers (required by Reddit API)
    headers = {
        'User-Agent': 'RedditReader/0.0.1'
    }

    # Send a POST request to obtain an access token from Reddit's API
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

    # Extract the access token from the response JSON
    TOKEN = res.json()['access_token']

    # Add the access token to the headers for authorization
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    
    return headers

def get_hot_posts(headers):
    # List to store data of posts
    post_data = []

    # Make a request for the trending posts in /r/Python
    res = requests.get("https://oauth.reddit.com/r/AmITheAsshole/hot",
                    headers=headers,
                    params={'limit':'1'})

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