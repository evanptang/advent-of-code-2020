import json

def check_for_qualifications_v1(lower_bound, upper_bound, character, password):
    count = password.count(character)
    if count >= lower_bound and count <= upper_bound:
        return True
    return False


def check_for_qualifications_v2(first_index, second_index, character, password):
    boolean_one = password[first_index-1] == character
    boolean_two = password[second_index-1] == character
    if boolean_one != boolean_two:
        return True
    return False


def range_to_bounds(str_range):
    parsed = str_range.split('-')
    for index, item in enumerate(parsed):
        parsed[index] = int(item)
    return parsed[0], parsed[1]

with open('parsed_dictionary.txt') as f:
    input_list = json.load(f)

count_v1 = 0
count_v2 = 0

for item in input_list:
    lower, upper = range_to_bounds(item['range'])
    if check_for_qualifications_v1(lower, upper, item['special_character'], item['password']):
        count_v1 += 1
    if check_for_qualifications_v2(lower, upper, item['special_character'], item['password']):
        count_v2 += 1


print(count_v2)
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.