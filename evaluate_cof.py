import json
import re
import openai
import datetime as dt
from pprint import pprint


def write_json(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=1)


def read_json(filename):
    with open(filename, 'r') as infile:
        return json.load(infile)


def read_file(filename):
    with open(filename, 'r') as infile:
        text = infile.read()
    return text


def query_gpt3(prompt):
    response = openai.Completion.create(
        engine='ada',
        prompt=prompt,
        temperature=0.5,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0.3,
        stop=['<<END>>', 'CONTEXT:', 'ACTION:', 'INSTRUCTIONS:'])
    return response['choices'][0]['text']


open_ai_api_key = read_file('openaiapikey.txt')
openai.api_key = open_ai_api_key
txt = str(dt.datetime.now())
action_fn = 'raw_actions/act_2021-04-18T10-33-04.json'
cof_fn = 'raw_cof/cof_%s.json' % txt.replace(':','-').replace(' ','T').split('.')[0]


def cof_evaluation(base, context, action):
    prompt = read_file(base)
    prompt = prompt % (context, action)
    response = query_gpt3(prompt)
    lines = response.splitlines()
    evaluation = lines[0].strip()
    explain = lines[1].replace('EXPLAIN:', '').strip()
    return evaluation, explain


if __name__ == '__main__':
    data = read_json(action_fn)
    output = list()
    for i in data:
        #print(i)
        #print('CONTEXT:', i['context'])
        for a in i['actions']:
            result = {'context': i['context'], 'action': a}
            # COF 1
            evaluation, explain = cof_evaluation('cof1_prompt.txt', i['context'], a)
            result['cof1_eval'] = evaluation
            result['cof1_explain'] = explain
            # COF 2
            evaluation, explain = cof_evaluation('cof2_prompt.txt', i['context'], a)
            result['cof2_eval'] = evaluation
            result['cof2_explain'] = explain
            # COF 3
            evaluation, explain = cof_evaluation('cof3_prompt.txt', i['context'], a)
            result['cof3_eval'] = evaluation
            result['cof3_explain'] = explain
            output.append(result)
            pprint(result)
    #pprint(output)
    write_json(cof_fn, output)