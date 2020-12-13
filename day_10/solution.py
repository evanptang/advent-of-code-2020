
def generate_list(file_name):
    output_list = list()
    with open(file_name) as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.strip()
            output_list.append(int(line))
    return output_list


def add_highest(lst):
    lst.append(lst[-1]+3)
    return lst

def add_lowest(lst):
    lst.insert(0,0)
    return lst

def calculate_interval(lst):
    interval_list = list()
    for index, item in enumerate(lst):
        if index == len(lst) -1:
            break
        interval_list.append(lst[index+1]-item)
    return interval_list


def get_count_from_intr(intr):
    return {i:intr.count(i) for i in intr}


def get_result_from_count(map):
    return map[1]*map[3]

if __name__ == '__main__':
    file_name = 'sample.txt'
    lst = sorted(generate_list(file_name))
    lst = add_highest(lst)
    lst = add_lowest(lst)
    # print(lst)
    intr = calculate_interval(lst)
    # print(intr)
    count = get_count_from_intr(intr)
    print(count)
    result = get_result_from_count(count)
    print(result)

    N = len(lst)
    print('N ', N)
    counts=[0] * N
    counts[-1]=1
    for i in range(N - 2, -1, -1):
        s = 0
        iter = 0
        for j in range(i + 1, N):
            iter += 1
            if lst[j] - lst[i] <= 3:
                s += counts[j]
            else:
                break
        counts[i] = s
    print(counts[0])
