import openai
from random import seed,sample
import os
import re


with open('openaiapikey.txt', 'r') as infile:
    open_ai_api_key = infile.read()
openai.api_key = open_ai_api_key


seed()
ctxdir = 'C:/CoreObjectiveFunctions/contexts/'
outdir = 'C:/CoreObjectiveFunctions/cof3/'
files = os.listdir(ctxdir)
files = [i for i in files if 'news' in i]    # filter list: dialog, medical, reddit, stack, news
prompt_name = 'COF3_prompt.txt'
files = sample(files, 65)
print(files)


def load_prompt(filename, payload):
    with open('C:/CoreObjectiveFunctions/%s' % filename, 'r', encoding='utf-8') as infile:
        body = infile.read().strip()
        body = body.replace('<<TEXT>>', payload)
        return body


def completion(prompt, engine='davinci', temp=0.7, top_p=1.0, tokens=300, freq_pen=0.0, pres_pen=0.0, stop=['\n\n', '<END>']):
    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=temp,
            max_tokens=tokens,
            top_p=top_p,
            frequency_penalty=freq_pen,
            presence_penalty=pres_pen,
            stop=stop)
        return response['choices'][0]['text'].strip()
    except Exception as oops:
        print('ERROR in completion function:', oops)


for f in files:
    try:
        with open(ctxdir + f, 'r', encoding='utf-8') as infile:
            context = infile.read()
        prompt = load_prompt(prompt_name, context)
        print('\n---------------------\n', context)
        cof = completion(prompt)
        if not cof:
            continue
        print('\n---------------------\n', cof)
        with open(outdir + f, 'w', encoding='utf-8') as outfile:
            outfile.write(cof)
    except Exception as oops:
        print('ERROR in main loop:', f, oops)