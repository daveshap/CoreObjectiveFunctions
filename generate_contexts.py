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
        max_tokens=200,
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
'weather',
'children',
'natural disasters',
'everyday problems',
'work',
'cooking',
'driving',
'neighbors',
'parents',
]


if __name__ == '__main__':
    for i in topics:
        prompt = base_prompt + i + '.\n\n-'
        print('PROMPT: ', prompt)
        content = query_gpt3(prompt)
        lines = content.splitlines() 
        for line in lines:
            line = line.strip()
            line = line.strip('-')
            line = line.strip()
            if len(line) == 0:
                continue
            print('LINE: ', line)
            append_file(contextfilename, line)