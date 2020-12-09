import json

file_name = 'parsed_sample.txt'
file_name = 'parsed_input.txt'

with open(file_name) as f:
    input_object = json.load(f)

def check_duplicates(list_obj):
    for item in list_obj:
        if list_obj.count(item) > 1:
            return True
    return False

lines_process = list()
before_end = 0
acc = 0
current_line = 0
while not check_duplicates(lines_process):
    before_end = acc
    lines_process.append(current_line)
    next_command = input_object[str(current_line)]
    if next_command[1][0] == '+':
        mult = 1
    else:
        mult = -1
    value = int(next_command[1][1:]) * mult
    
    if next_command[0] == 'nop':
        current_line = current_line + 1
    elif next_command[0] == 'acc':
        acc = acc + value
        current_line = current_line + 1
        print(f'acc = {acc}')
    elif next_command[0] == 'jmp':
        current_line = current_line + value

print(before_end)

