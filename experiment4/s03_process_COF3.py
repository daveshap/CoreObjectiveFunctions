import re
import os
from gpt3_functions import gpt3_completion
import random


post_dir = 'posts/'
src_dir = 'cof1/'
out_dir = 'cof3/'


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


if __name__ == '__main__':
    filelist = os.listdir(src_dir)
    for filename in filelist:
        try:
            body = open_file(post_dir + filename)
            # generate internet search queries
            prompt = open_file('cof3_a.txt')
            prompt = prompt.replace('<<TEXT>>', body)
            queries = gpt3_completion(prompt)
            print('\n\nResponse:', queries)
            if not queries:
                continue
            # answer search queries
            prompt = open_file('cof3_b.txt')
            prompt = prompt.replace('<<TEXT>>', queries)
            answers = gpt3_completion(prompt)
            print('\n\nResponse:', answers)
            if not answers:
                continue
            # add more info:
            prompt = open_file('cof3_c.txt')
            prompt = prompt.replace('<<TEXT>>', queries)
            prompt = prompt.replace('<<PARAGRAPH>>', answers)
            specifics = gpt3_completion(prompt)
            print('\n\nResponse:', specifics)
            if not specifics:
                continue
            # compose final output
            final = answers + specifics
            final = re.sub('\s+', ' ', final)
            with open('%s/%s' % (out_dir, filename), 'w', encoding='utf-8') as outfile:
                outfile.write(final)
        except Exception as oops:
            print(oops)