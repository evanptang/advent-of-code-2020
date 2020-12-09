import json
import copy

# file_name = 'parsed_sample.txt'
file_name = 'parsed_input.txt'
file_name = 'parsed_testing.txt'

with open(file_name) as f:
    input_obj = json.load(f)
    
def replace_one_operation(input_object):
    """
    iteratively replaces one operation
    """
    current_index = 0
    intro = copy.deepcopy(input_object)
    while not terminates_at_ends(intro):
        intro = copy.deepcopy(input_object)
        list_object = (generate_list(intro))
        next_jmp = find_next_nop_jmp(list_object, current_index)
        # print(f'list_object[next_jmp] {list_object[next_jmp] }')
        if list_object[next_jmp][0] == 'nop':
            intro[str(next_jmp)][0] = 'jmp'
            current_index = find_next_nop_jmp(list_object, current_index + 1)
            try:
                current_index = find_next_nop_jmp(list_object, current_index + 1)
            except:
                current_index = current_index
        else:
            intro[str(next_jmp)][0] = 'nop'
            try:
                current_index = find_next_nop_jmp(list_object, current_index + 1)
            except:
                current_index = current_index
        print('current index:', str(current_index))
        # print(f'intro: {intro}')
    return calculate_result(intro)

def find_next_nop_jmp(list_object, current_index):
    while list_object[current_index][0] == 'acc':
        current_index += 1
    return current_index



def generate_list(input_object):
    output_list = list()
    for i in range(len(input_obj)):
        str_index = str(i)
        output_list.append(input_obj[str_index])
    return output_list

def calculate_result(input_object):
    acc = 0
    current_line = 0
    while current_line != len(input_obj) -1:
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
        elif next_command[0] == 'jmp':
            current_line = current_line + value
    next_command = input_object[str(current_line)]
    if next_command[1][0] == '+':
        mult = 1
    else:
        mult = -1
    value = int(next_command[1][1:]) * mult
    if next_command[0] == 'acc':
        acc = acc + value
        current_line = current_line + 1
    return acc



def check_duplicates(list_obj):
    for item in list_obj:
        if list_obj.count(item) > 1:
            return True
    return False

def terminates_at_ends_int(input_object):
    """
    Runs through the list. Returns True if terminates at the end
    """
    lines_process = list()
    acc = 0
    current_line = 0
    while not check_duplicates(lines_process):
        if current_line == len(input_object) - 1:
            return True
        lines_process.append(current_line)
        next_command = input_object[current_line]
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
        elif next_command[0] == 'jmp':
            current_line = current_line + value
    return False

def terminates_at_ends(input_object):
    """
    Runs through the list. Returns True if terminates at the end
    """
    lines_process = list()
    acc = 0
    current_line = 0
    while not check_duplicates(lines_process):
        if current_line == len(input_object) - 1:
            return True
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
        elif next_command[0] == 'jmp':
            current_line = current_line + value
    return False

# print(replace_one_operation(input_obj))
print(calculate_result(input_obj))