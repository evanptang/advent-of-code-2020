import copy

def parse_input(file_name):
    output_list = list()
    with open(file_name) as f:
        for line in f:
            line_list = list()
            line = line.replace('\n', '')
            for char in line:
                if char == 'L':
                    line_list.append(0)
                elif char == '.':
                    line_list.append(None)
                else:
                    raise RuntimeError(f'Unexpected Character:{char}')
            output_list.append(line_list)
    return output_list


def query_adjacent_neighbors(x, y, max_x, max_y):
    if x == 0:
        x_list = [0, 1]
    elif x == max_x:
        x_list = [max_x, max_x -1]
    else:
        x_list = [x-1, x, x+1]

    if y == 0:
        y_list = [0, 1]
    elif y == max_y:
        y_list = [max_y, max_y - 1]
    else:
        y_list = [y-1, y, y+1]

    output_list = list()

    for item_x in x_list:
        for item_y in y_list:
            if item_x != x or item_y != y:
                output_list.append((item_x, item_y))
    return output_list


def parse_through_visible_neighbors(all_lists, nested_list):
    acc = 0
    for item in all_lists:
        row_val = parse_row(item, nested_list)
        if row_val:
            acc += row_val
    return acc


def parse_row(row, nested_list):
    for i in row:
        i_x, i_y = i
        val = query_value(i_x, i_y, nested_list)
        if val is None:
            continue
        return val

def query_visible_neighbors(x, y, nested_list):
    hor_bot, hor_top = get_horizontal(x, y, nested_list)
    ver_bot, ver_top = get_vertical(x, y, nested_list)
    upper_right_diag, upper_left_diag, lower_right_diag, lower_left_diag = get_diagonal(x, y, nested_list)
    hor_bot.reverse()
    ver_bot.reverse()
    return [hor_bot, hor_top, ver_bot, ver_top, upper_right_diag, upper_left_diag, lower_right_diag, lower_left_diag]

def get_horizontal(x, y, nested_list):
    bottom_list = list()
    top_list = list()
    for iter_x in range(x):
        if iter_x != x:
            bottom_list.append((iter_x, y))
    for iter_x in range(x, len(nested_list[0]), 1):
        if iter_x != x:
            top_list.append((iter_x, y))
    return bottom_list, top_list
        

def get_vertical(x, y, nested_list):
    bottom_list = list()
    top_list = list()
    for iter_y in range(y):
        if iter_y != y:
            bottom_list.append((x, iter_y))
    for iter_y in range(y, len(nested_list), 1):
        if iter_y != y:
            top_list.append((x, iter_y))
    return bottom_list, top_list

def get_diagonal(x, y, nested_list):
    upper_right_diag = list()
    upper_left_diag = list()
    lower_right_diag = list()
    lower_left_diag = list()

    x_away = 0
    for iter_x in range(x, -1, -1):
        if iter_x == x:
            continue
        x_away += 1
        if is_valid_pos(iter_x, y+x_away, nested_list):
            lower_right_diag.append((iter_x, y+x_away))
        if is_valid_pos(iter_x, y-x_away, nested_list):
            upper_right_diag.append((iter_x, y-x_away))
    x_away = 0
    for iter_x in range(x, len(nested_list), 1):
        if iter_x == x:
            continue
        x_away += 1
        if is_valid_pos(iter_x, y+x_away, nested_list):
            lower_left_diag.append((iter_x, y+x_away))
        if is_valid_pos(iter_x, y-x_away, nested_list):
            upper_left_diag.append((iter_x, y-x_away))
    return upper_right_diag, upper_left_diag, lower_right_diag, lower_left_diag


def is_valid_pos(x, y, nested_list):
    max_x = len(nested_list[0])
    max_y = len(nested_list)
    if x >=0 and x< max_x and y >=0 and y < max_y:
        return True
    return False

def query_value(x, y, nested_list):
    return nested_list[y][x]


def accumulate_value(neighbors_list, nested_list):
    accumulator = 0
    for item in neighbors_list:
        val = query_value(item[0], item[1], nested_list)
        if val:
            accumulator += val
    return accumulator


def accumulate_visible_value(directional_list, nested_list):
    accumulator = 0
    for item in directional_list:
        val = query_value(item[0], item[1], nested_list)
        if val:
            accumulator += val
    if accumulator > 0:
        return 1
    return 0


def change_pos(x, y, nested_list):
    val = query_value(x, y, nested_list)
    if val == 0:
        nested_list[y][x] = 1
    elif val == 1:
        nested_list[y][x] = 0
    else:
        nested_list[y][x] = None
    return nested_list


def walk_through_adjacent(parsed_input):
    output = copy.deepcopy(parsed_input)
    for iter_y in range(len(parsed_input)):
        for iter_x in range(len(parsed_input[0])):
            pos = query_value(iter_x, iter_y, parsed_input)
            if pos is None:
                continue
            neighbors = query_adjacent_neighbors(iter_x, iter_y, len(parsed_input[0])-1 , len(parsed_input)-1)
            accum = accumulate_value(neighbors, parsed_input)
            if pos == 0 and accum == 0:
                output = change_pos(iter_x, iter_y, output)
            elif pos == 1 and accum >= 4:
                output = change_pos(iter_x, iter_y, output)
    return output

        
def walk_through_visible(parsed_input):
    output = copy.deepcopy(parsed_input)
    for iter_y in range(len(parsed_input)):
        for iter_x in range(len(parsed_input[0])):
            pos = query_value(iter_x, iter_y, parsed_input)
            if pos is None:
                continue
            neighbors = query_visible_neighbors(iter_x, iter_y, parsed_input)
            accum = parse_through_visible_neighbors(neighbors, parsed_input)
            if pos == 0 and accum == 0:
                output = change_pos(iter_x, iter_y, output)
            elif pos == 1 and accum >= 5:
                output = change_pos(iter_x, iter_y, output)
    return output


def find_num_occupied(nested_list):
    occupied = 0
    for iter_y in range(len(nested_list)):
        for iter_x in range(len(nested_list[0])):
            pos = query_value(iter_x, iter_y, nested_list)
            if pos is not None:
                occupied += pos
    return occupied


def iterate_through_adjacent(parsed_input):
    iter_1 = walk_through_adjacent(parsed_input)
    occ_1 = find_num_occupied(iter_1)
    iter_x = walk_through_adjacent(iter_1)
    occ_2 = find_num_occupied(iter_x)
    iteration = 2
    while occ_1 != occ_2:
        print(f"Occupied 1: {str(occ_1)}, Occupied 2: {str(occ_2)}")
        print('iteration:', iteration)
        occ_1 = occ_2
        iteration += 1
        iter_x = walk_through_adjacent(iter_x)
        occ_2 = find_num_occupied(iter_x)
    print(occ_2)
    return occ_2



def iterate_through_visible(parsed_input):
    iter_1 = walk_through_visible(parsed_input)
    occ_1 = find_num_occupied(iter_1)
    iter_x = walk_through_visible(iter_1)
    occ_2 = find_num_occupied(iter_x)
    iteration = 2
    while occ_1 != occ_2:
        print(f"Occupied 1: {str(occ_1)}, Occupied 2: {str(occ_2)}")
        print('iteration:', iteration)
        occ_1 = occ_2
        iteration += 1
        iter_x = walk_through_visible(iter_x)
        occ_2 = find_num_occupied(iter_x)
    return occ_2


if __name__ == '__main__':
    file_name = 'sample.txt'
    parsed = parse_input(file_name)
    print(iterate_through_visible(parsed))
