import requests
from pprint import pprint

def get_top_n_posts(subreddit, n):
    """
    returns the top n posts from a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-agent': 'Bleep blorp bot 0.1'}
    params = {'limit': n}
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 200:
        return res.json()


data = get_top_n_posts('Anxiety', 10)
#pprint(data)
#pprint(data['data']['children'][0]['data']['permalink'])

for child in data['data']['children']:
    print(child['data']['permalink'])