import json
import copy

input_file = 'parsed_input.txt'
with open(input_file) as f:
    input_json = json.load(f)

secondary = copy.deepcopy(input_json)

characteristic = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt', 'cid']

not_valid = 0
strict_valid = 0
for index, item in enumerate(input_json):
    for character in characteristic:
        if character not in item.keys():
            if character != 'cid':
                not_valid += 1
                secondary.remove(item)
                # print(f'item: {item}')
                # print(f'character: {character}')
                break


# for item in input_json:

valid = len(input_json) - not_valid
            
for item in secondary:
    if item['byr'] > 2002 or item['byr'] < 1920:
        continue
    if item['iyr'] < 2010 or item['iyr'] > 2020:
        continue
    if item['eyr'] > 2030 or item['eyr'] < 2020:
        continue
    height = item['hgt']
    measures = ['cm', 'in']
    try:
        h_num = height[:-2]
        h_measure = height[-2:]
        if h_measure not in measures:
            continue
        try:
            val = int(h_num)
            if h_measure == 'cm':
                if val > 193 or val < 150:
                    continue
            else:
                if val > 76 or val < 59:
                    continue
        except ValueError:
            continue
    except:
        print(f'height: {height}')
        continue
    try:
        if item['hcl'][0] != '#':
            continue
        if len(item['hcl']) != 7:
            continue
        try:
            int(item['hcl'][1:], 16)
        except:
            print(item['hcl'][1:])
            continue
    except:
        print(f"failed hcl: {item['hcl']}")
    eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if item['ecl'] not in eye_color:
        continue
    if len(item['pid']) != 9:
        print(f"len pid :{str(len(item['pid']))}")
        continue
    try:
        int(item['pid'])
    except ValueError:
        continue
    strict_valid += 1

print(strict_valid)
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.