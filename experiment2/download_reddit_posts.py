from pprint import pprint as pp
import requests
from uuid import uuid4


def scrape_reddit(subreddit, period):
    url = 'https://www.reddit.com/r/{}/top/.json?t={}'.format(subreddit, period)  # hour, day, week, month, all
    headers = {'User-agent': 'CoreObjectiveFunctionBot'}
    params = {'limit': 100000}
    info = requests.get(url, headers=headers, params=params)
    return info.json()['data']['children']


#data = scrape_reddit('depression_help', 'day')
#posts = data['data']['children']
#pp(data)

#posts = scrape_reddit('depression_help', 'day')

#for post in posts:
#    print(post['data']['title'])
#    print(post['data']['selftext'])
#    print('################')
#    print('################')
#    print('################')


def load_subs():
    with open('subreddits.txt.', 'r', encoding='utf-8') as infile:
        return infile.read().splitlines()
        
subs = load_subs()

for subreddit in subs:
    posts = scrape_reddit(subreddit, 'month')
    print(subreddit)
    for post in posts:
        body = '{}\n{}'.format(post['data']['title'].strip(), post['data']['selftext'].strip())
        print(post['data']['title'])
        with open('posts/{}_{}.txt'.format(subreddit, str(uuid4())), 'w', encoding='utf-8') as outfile:
            outfile.write(body)