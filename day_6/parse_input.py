import json

# file_name = 'sample.txt'
file_name = 'input.txt'

final_object = list()
with open(f'parsed_{file_name}', 'w+') as f:
    with open(file_name) as g:
        temp = list()
        for line in g:
            line = line.replace('\n', '')
            if line == '':
                final_object.append(temp)
                temp = list()
                continue
            temp.append(line)
                
        final_object.append(temp)
    json.dump(final_object, f)