import json

input_file = 'sample.txt'

final_list = list()

with open(f'parsed_{input_file}', 'w+') as f:
    with open(input_file) as g:
        temp = dict()
        g_lines = g.readlines()
        last = g_lines[-1]
        for index, original_line in enumerate(g_lines):
            line = original_line.replace('\n', '')
            if line == '':
                final_list.append(temp)
                temp = dict()
                continue
            line = line.split(' ')
            for item in line:
                item = item.split(':')
                if item[0] != 'pid':
                    try:
                        val = int(item[1])
                    except:
                        val = item[1]
                else:
                    val = item[1]
                temp[item[0]] = val
            if original_line == last:
                final_list.append(temp)

    json.dump(final_list, f)
