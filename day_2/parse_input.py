import json

with open('parsed_dictionary.txt', 'w+') as f:
    output_list = list()
    with open('input.txt') as g:
        for line in g:
            line = line.replace(':', '')
            line = line.replace('\n', '')
            input_list = (line.split(' '))
            output_dictionary = dict()
            output_dictionary['range'] = input_list[0]
            output_dictionary['special_character'] = input_list[1]
            output_dictionary['password'] = input_list[2]
            output_list.append(output_dictionary)
    json.dump(output_list, f)