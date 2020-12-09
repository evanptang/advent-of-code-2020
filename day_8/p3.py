import subprocess
from p2 import terminates_at_ends_int

def reset():
    subprocess.run(
        [
            'rm', 
            'testing.txt'
        ]
    )

def munge_data():
    collector = dict()
    with open('testing.txt') as f:
        for index, line in enumerate(f):
            line = line.replace('\n', '')
            line = line.split(' ')
            collector[int(index)] = (line)
        return collector

def run_through_line(cur):
    while not terminates_at_ends_int(munge_data()):
        reset()
        with open('testing.txt', 'w+') as g:
            with open('input.txt') as f:
                for index, line in enumerate(f):
                    if index == cur:
                        if line[:3] == 'nop':
                            line = line.replace('nop', 'jmp')
                        elif line[:3] == 'jmp':
                            line = line.replace('jmp', 'nop')
                        else:
                            cur = cur + 1
                    g.write(line)
                cur = cur + 1
                print(cur)

run_through_line(0)
