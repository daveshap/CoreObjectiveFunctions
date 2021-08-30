import os


fixdir = 'C:/CoreObjectiveFunctions/identify_cof1/'
files = os.listdir(fixdir)


for f in files:
    with open(fixdir + f, 'r', encoding='utf-8') as infile:
        body = infile.read()
    body = body.replace('..', '.')
    body = body.replace('..', '.')
    body = body.replace('?.', '.')
    body = body.replace('!.', '.')
    body = body.replace(',.', '.')
    with open(fixdir + f, 'w', encoding='utf-8') as outfile:
        outfile.write(body)