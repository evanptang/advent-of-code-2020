import json

inputs = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

file_path = 'parsed_input.txt'
with open(file_path) as f:
    input_list = json.load(f)

def is_x_y_tree(x, y):
    if input_list[y][x] == '#':
        return True
    return False


def next_position(x, y, x_increment, y_increment, height, width):
    y_final =  y + y_increment 
    x_final = (x + x_increment) % width

    if y_final >= height:
        return False
    return [x_final, y_final]

def calculate_trees(init_x, init_y, x_increment, y_increment, nested_input):
    count = 0
    cursor = next_position(init_x, init_y, x_increment, y_increment, len(nested_input), len(nested_input[0]))
    while cursor:
        if is_x_y_tree(cursor[0], cursor[1]):
            count += 1 
        cursor = next_position(cursor[0], cursor[1], x_increment, y_increment, len(nested_input), len(nested_input[0]))
    return count

product = 1
for i in inputs:
    product = product * calculate_trees(0, 0, i[0], i[1], input_list)

print(product)