import json

file_name = 'sample.txt'
# file_name = 'input.txt'

final_object = dict()
with open(f'parsed_{file_name}', 'w+') as f:
    with open(file_name) as g:
        for line in g:
            line = line.replace('\n', '')
            line = line.replace('bags', 'bag')
            line = line.replace('.', '')
            line = line.split('contain')
            line[0] = line[0][:-1]
            line[1] = line[1].split(',')
            temp = dict()
            try:
                for item in line[1]:
                    item = item[1:]
                    temp[item[2:]] = int(item[0])
            except:
                temp = {}
            line[1] = temp
            final_object[line[0]] = line[1]
    json.dump(final_object, f)