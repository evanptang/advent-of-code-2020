import json
file_path = 'input.txt'

with open (f'parsed_{file_path}', 'w+') as f:
    output_list = list()
    with open(file_path) as g:
        for line in g:
            line = line.replace('\n', '')
            output_list.append(list(line))
    json.dump(output_list, f)