import re
import os
from gpt3_functions import gpt3_completion
import random


post_dir = 'posts/'
src_dir = 'cof1/'
out_dir = 'cof2/'


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


if __name__ == '__main__':
    filelist = os.listdir(src_dir)
    for filename in filelist:
        try:
            body = open_file(post_dir + filename)
            prompt = open_file('cof2.txt')
            prompt = prompt.replace('<<TEXT>>', body)
            response = gpt3_completion(prompt)
            print('\n\nResponse:', response)
            if not response:
                continue
            with open('%s/%s' % (out_dir, filename), 'w', encoding='utf-8') as outfile:
                outfile.write(response)
        except Exception as oops:
            print(oops)