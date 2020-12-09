import json 

# file_name = 'parsed_sample.txt'
file_name = 'parsed_input.txt'

with open(file_name) as f:
    input_object = json.load(f)

def calculate_row(str_row):
    min_v = 0 
    max_v = 127
    for char in str_row:
        if char == 'F':
            min_v = min_v
            max_v = ((((max_v-min_v)+1)/2)-1) + min_v
        else:
            min_v = (((max_v-min_v)+1)/2) + min_v
            max_v = max_v
        # print(f'min_v: {min_v}')
        # print(f'max_v: {max_v}')
        # print(char)
        if min_v == max_v:
            break
    return int(min_v)

def calculate_col(str_col):
    min_v = 0 
    max_v = 7
    for char in str_col:
        if char == 'L':
            min_v = min_v
            max_v = ((((max_v-min_v)+1)/2)-1) + min_v
        else:
            min_v = (((max_v-min_v)+1)/2) + min_v
            max_v = max_v
        # print(f'min_v: {min_v}')
        # print(f'max_v: {max_v}')
        # print(char)
        if min_v == max_v:
            break
    return int(min_v)


def calculate_val(row, col):
    return row*8 + col

# max_v = 0
# for pair in input_object:
#     row = pair[0]
#     col = pair[1]
#     val = calculate_val(
#         calculate_row(row),
#         calculate_col(col)
#     )
#     if val > max_v:
#         print(max_v)

#         max_v = val
# print(f'max_v: {max_v}')

seat_map = dict()
for pair in input_object:
    row = calculate_row(pair[0])
    col = calculate_col(pair[1])
    if row not in seat_map:
        seat_map[row] = [col]
    else:
        seat_map[row].append(col)

for r, c in seat_map.items():
    if len(c) < 8:
        print(f'row: {r}')
        print(f'col: {c}')
        print(f'len: {str(len(c))}\n')

print(calculate_val(67, 3))
