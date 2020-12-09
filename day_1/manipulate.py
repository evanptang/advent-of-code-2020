with open('final_input', 'w+') as f:
    f.write('[')
    with open('input.txt') as g:
        for i in g:
            i = i.replace('\n', ',')
            f.write(i)
    f.write(']')