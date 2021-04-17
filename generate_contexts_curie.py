import re
import openai
import datetime as dt


def read_file(filename):
    with open(filename, 'r') as infile:
        text = infile.read()
    return text


def append_file(filename, text):
    with open(filename, 'a') as outfile:
        outfile.write(text)
        outfile.write('\n')


def query_gpt3(prompt):
    response = openai.Completion.create(
        engine='curie-instruct-beta',
        prompt=prompt,
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0.3,
        stop=['<<END>>', 'CONTEXT:', 'ACTION:', 'INSTRUCTIONS:'])
    return response['choices'][0]['text']


open_ai_api_key = read_file('openaiapikey.txt')
openai.api_key = open_ai_api_key
txt = str(dt.datetime.now())
contextfilename = 'raw_contexts/ctx_%s.txt' % txt.replace(':','-').replace(' ','T').split('.')[0]
original_prompt = 'Write a list of random scenarios.'
base_prompt = 'Write a list of random scenarios about '


topics = [
'the weather',
'children',
'natural disasters',
'everyday problems',
'work',
'cooking',
'driving',
'neighbors',
'parents',
'the economy',
'my career',
'dogs',
'home ownership',
'being bored',
'being sick',
'being tired',
'being angry',
]


def clean_line(txt):
    # clean off hyphen
    txt = txt.strip()
    txt = txt.strip('-')
    txt = txt.strip()
    # clean off numbered list
    digit = re.match('''^\d+\.\s*''', txt)
    if digit:
        txt = txt.replace(digit.group(), '')
    return txt
    

def generate_contexts(prompt):
    print('PROMPT: ', prompt)
    content = query_gpt3(prompt)
    lines = content.splitlines() 
    for line in lines:
        line = clean_line(line)
        if len(line) == 0:
            continue
        print('LINE: ', line)
        append_file(contextfilename, line)


if __name__ == '__main__':
    generate_contexts(original_prompt)
    for i in topics:
        prompt = base_prompt + i + '.\n\n-'
        generate_contexts(prompt)