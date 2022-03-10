import os


post_dir = 'posts/'
cofs = ['cof1', 'cof2', 'cof3']
out_dir = 'compiled/'


if __name__ == '__main__':
    filelist = os.listdir('cof1/')
    for filename in filelist:
        try:
            with open(post_dir + filename, 'r', encoding='utf-8') as infile:
                scenario = infile.read()
            with open('cof1/' + filename, 'r', encoding='utf-8') as infile:
                cof1 = infile.read()
            with open('cof2/' + filename, 'r', encoding='utf-8') as infile:
                cof2 = infile.read()
            with open('cof3/' + filename, 'r', encoding='utf-8') as infile:
                cof3 = infile.read()
            body = '''Process the Core Objective Functions (reduce suffering, increase prosperity, increase understanding) on the following scenario:\n\n%s\n\nReduce suffering: %s\n\nIncrease prosperity: %s\n\nIncrease understanding: %s''' % (scenario, cof1, cof2, cof3)
            with open(out_dir + filename, 'w', encoding='utf-8') as outfile:
                outfile.write(body)
        except Exception as oops:
            print(oops)