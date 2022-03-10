import re
import os
from gpt3_functions import gpt3_completion
import random


post_dir = 'posts/'
cofs = ['cof1', 'cof2', 'cof3']


def load_subs():
    with open('subreddits.txt', 'r', encoding='utf-8') as infile:
        return reversed(infile.read().splitlines())


if __name__ == '__main__':
    subs = load_subs()
    for sub in subs:
        print('Subreddit:', sub)
        # pick a random post from the given subreddit
        random.seed()
        files = os.listdir(post_dir)
        files = [i for i in files if sub in i]
        file = random.choice(files)
        with open(post_dir+file, 'r', encoding='utf-8') as infile:
            body = infile.read()
        print('\n\nPost:', body)
        # perform each COF on the post
        for cof in cofs:
            with open('%s.txt' % cof, 'r', encoding='utf-8') as infile:
                prompt = infile.read()
            prompt = prompt.replace('<<TEXT>>', body)
            response = gpt3_completion(prompt)
            print('\n\nResponse:', response)
            if not response:
                continue
            with open('%s/%s' % (cof, file), 'w', encoding='utf-8') as outfile:
                outfile.write(response)