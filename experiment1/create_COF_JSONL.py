import os
import json


ctxdir = 'C:/CoreObjectiveFunctions/contexts/'
cofdir1 = 'C:/CoreObjectiveFunctions/cof1/'
cofdir2 = 'C:/CoreObjectiveFunctions/cof2/'
cofdir3 = 'C:/CoreObjectiveFunctions/cof3/'


data = list()

def process_cof(ctxdir, cofdir, label):
    files = os.listdir(cofdir)
    for f in files:
        with open(cofdir + f, 'r', encoding='utf-8') as infile:
            cof = infile.read()
        with open(ctxdir + f, 'r', encoding='utf-8') as infile:
            context = infile.read()
        prompt = '%s\n%s:' % (context, label)
        info = {'prompt': prompt, 'completion': cof}
        data.append(info)


process_cof(ctxdir, cofdir1, 'Reduce suffering')
process_cof(ctxdir, cofdir2, 'Increase prosperity')
process_cof(ctxdir, cofdir3, 'Increase understanding')


with open('cof.jsonl', 'w') as outfile:
    for i in data:
        json.dump(i, outfile)
        outfile.write('\n')