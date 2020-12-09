import json

# file_name = 'sample.txt'
# file_name = 'input.txt'
file_name = 'testing.txt'

collector = dict()
with open(file_name) as f:
    for index, line in enumerate(f):
        line = line.replace('\n', '')
        line = line.split(' ')
        collector[int(index)] = (line)

with open(f'parsed_{file_name}', 'w+') as f:
    json.dump(collector, f)
