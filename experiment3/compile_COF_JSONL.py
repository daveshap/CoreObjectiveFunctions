import os
import json
import re


cofdir1 = 'C:/CoreObjectiveFunctions/experiment2/cof1/'
cofdir2 = 'C:/CoreObjectiveFunctions/experiment2/cof2/'
cofdir3 = 'C:/CoreObjectiveFunctions/experiment2/cof3/'


data = list()


def process_cof(cofdir, label):
    files = os.listdir(cofdir)
    for f in files:
        with open(cofdir + f, 'r', encoding='utf-8') as infile:
            cof = infile.read()
        l = re.split('Ideas.*:', cof)
        prompt = label + '\n\n' + re.sub('.*Generate some ideas.', '', l[0]).strip() + '\n\n' + label + ':'
        completion = '\n' + l[1].replace('-', '- ').replace('-  ', '- ').strip()
        info = {'prompt': prompt, 'completion': completion}
        data.append(info)


process_cof(cofdir1, 'Reduce suffering')
process_cof(cofdir2, 'Increase prosperity')
process_cof(cofdir3, 'Increase understanding')


with open('cof.jsonl', 'w') as outfile:
    for i in data:
        json.dump(i, outfile)
        outfile.write('\n')