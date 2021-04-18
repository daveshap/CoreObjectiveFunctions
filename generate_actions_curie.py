import json
import re
import openai
import datetime as dt


def write_json(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=1)


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
contextfilename = 'raw_contexts/ctx_2021-04-17T10-10-12.txt'
actionfilename = 'raw_actions/act_%s.json' % txt.replace(':','-').replace(' ','T').split('.')[0]


base_prompt = '''Generate a list of possible actions in response to the context. 

CONTEXT: %s
ACTION:'''

# TODO experiment with prompts (some specific for dialog, some for Raven POV, etc)


def clean_line(txt):
    txt = txt.replace('ACTION:', '')
    # clean off hyphen
    txt = txt.strip()
    txt = txt.strip('-')
    txt = txt.strip()
    # clean off numbered list
    digit = re.match('''^\d+.?\s*''', txt)
    if digit:
        txt = txt.replace(digit.group(), '')
    # clean off lettered list
    letter = re.match('''^\w\)\s*''', txt)
    if letter:
        txt = txt.replace(letter.group(), '')
    return txt
    

def generate_actions(prompt):
    result = list()
    content = query_gpt3(prompt)
    lines = content.splitlines() 
    for line in lines:
        line = clean_line(line)
        if len(line) == 0:
            continue
        print('ACTION: ', line)
        result.append(line)
    return result


if __name__ == '__main__':
    data = list()
    contexts = read_file(contextfilename)
    for i in contexts.splitlines():
        print('\n\nCONTEXT: ', i)
        prompt = base_prompt % i
        actions = generate_actions(prompt)
        data.append({'context': i, 'actions': actions})
    write_json(actionfilename, data)