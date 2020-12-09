import json
import copy

# file_name = 'parsed_sample.txt'
file_name = 'parsed_input.txt'

with open(file_name) as f:
    input_obj = json.load(f)

def find_preamble(index, list_obj, preamble_len=25):
    # print(list_obj)
    return list_obj[index-preamble_len:index]


def valid_value(preamble, value):
    nums = list()
    for index, item in enumerate(preamble):
        if index == len(preamble) - 1:
            break
        for item_inner in preamble[index+1:]:
            # print(f'item: {item}, inner_item: {item_inner}')
            sum_v = item + item_inner
            if sum_v not in nums:
                nums.append(sum_v)
    return value in nums 


def find_first_no_op(input_object, start):
    while valid_value(find_preamble(start, input_object), input_object[start]):
        start += 1
        # print(f"iteration: {start}")
    return input_obj[start]

# print(find_first_no_op(input_obj, 25))
# 26134589

def generate_sum(start_index, end_index, list_obj):
    return sum(list_obj[start_index:end_index])


def find_window(input_object, target):
    for index, value in enumerate(input_object):
        for sub_index, sub_value in  enumerate(input_object[index:]):
            summed = generate_sum(index, sub_index, input_object)
            if summed == target:
                window = input_obj[index:sub_index]
                return max(window) + min(window)
            elif summed > target:
                # print('out of index')
                break

print(find_window(input_obj, 26134589))
