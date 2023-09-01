import requests
import config

auth = requests.auth.HTTPBasicAuth(config.REDDIT_CLIENT_ID, config.REDDIT_SECRET_KEY)

data = {'grant_type': 'password',
        'username': config.REDDIT_USERNAME,
        'password': config.REDDIT_PASSWORD}

headers = {'User-Agent': 'RedditReader/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

print("ALL GOOD")