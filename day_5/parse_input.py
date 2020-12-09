import json

# file_name = 'sample.txt'
file_name = 'input.txt'

final_object = list()
with open(f'parsed_{file_name}', 'w+') as f:
    with open(file_name) as g:
        for line in g:
            line = line.replace('\n', '')
            first_7 = line[:7]
            last_7 = line[7:]
            temp = [first_7, last_7]
            final_object.append(temp)
            
    json.dump(final_object, f)