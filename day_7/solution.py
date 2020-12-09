import json 

# file_name = 'parsed_sample.txt'
file_name = 'parsed_input.txt'

with open(file_name) as f:
    input_object = json.load(f)

bag = 'shiny gold bag'

def query_bag(bag, dictionary, input_object):
    if bag in dictionary:
        return True
    elif len(dictionary) == 0:
        return False
    else:
        for key, _ in dictionary.items():
            # print(f'input_object[key]: {input_object[key]}')
            return query_bag(bag, input_object[key], input_object)

def find_all_bags(dictionary, input_object, total):
    for key, _ in dictionary.items():
        if key not in total:
            find_all_bags(input_object[key], input_object, total)
            total.append(key)
    return total


count = 0

def return_bags(dictionary, input_object):
    if len(dictionary) == 0:
        return 1
    for key, value in dictionary.items():
        print(f'key: {key}, value: {value}')
        return value * return_bags(input_object[key], input_object) + count + 1
# for key, value in input_object.items():
#     all_bags  = find_all_bags(value, input_object, [])
#     if bag in all_bags:
#         count = count + 1
    # print(f'key: {key}, value: {value}')
#     if query_bag(bag, value, input_object):
#         # print(f'{key} containts {bag}')
#         count += 1

print(return_bags(input_object[bag], input_object))


# print(f'count: {str(count)}')