import json

file_name = 'sample.txt'
file_name = 'input.txt'
output = list()
with open(file_name) as f:
    for line in f:
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        output.append(int(line))

with open(f'parsed_{file_name}', 'w+') as f:
    json.dump(output, f)