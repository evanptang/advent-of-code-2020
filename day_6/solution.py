import json 

# file_name = 'parsed_sample.txt'
file_name = 'parsed_input.txt'

with open(file_name) as f:
    input_object = json.load(f)

count = 0
for li in input_object:
    hash_map = dict()
    for item in li:
        for char in item:
            if char not in hash_map:
                hash_map[char] = 1
            else:
                hash_map[char] = hash_map[char] + 1
        
    for key, value in hash_map.items():
        if value == len(li):
            count = count + 1  


print(count)

