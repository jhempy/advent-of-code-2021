# day22_part1.py

from collections import Counter
import numpy as np

instructions = []
magic = 101
reactor = np.zeros([magic, magic, magic]) # to represent -50..50 in each axis

def lit():
    global magic, reactor
    lit = 0
    for x in range(0, magic):
        for y in range(0, magic):
            for z in range(0, magic):
                lit = lit + reactor[x,y,z]
    return int(lit)

def correct_boundaries(b):
    global magic
    c = []
    if b[0] >= magic:
        # x starts too high
        return []
    if b[2] >= magic:
        # y starts too high
        return []
    if b[4] >= magic:
        # z starts too high
        return []
    if b[1] < 0:
        # x ends too low
        return []
    if b[3] < 0:
        # y ends too low
        return []
    if b[5] < 0:
        # z ends too low
        return []
    # if we are still here, then x, y, and z contain some overlap with the range
    # restrict them
    for val in b:
        if val >= magic:
            c.append(magic)
        elif val < 0:
            c.append(0)
        else:
            c.append(val)
    return c


def convert_coord(x):
    global magic
    return int(x) + 50
    
def parse_input_file(file): 
    global instructions, reactor
    f = open(file, "r")
    for (i, line) in enumerate(f):
        l = line.rstrip('\n')
        status, temp = l.split(' ')
        ranges = temp.split(',')
        boundaries = []
        for r in ranges:
            a, b = r.split('=')
            b = b.split('..')
            boundaries.append(convert_coord(b[0]))
            boundaries.append(convert_coord(b[1]))
        boundaries = correct_boundaries(boundaries)
        if boundaries:
            instructions.append([1 if status == 'on' else 0, boundaries])
    f.close()

def print_reactor():
    global reactor
    print(f'--------------------')
    print(f'INFO > Reactor:')
    print(reactor)
    print(f'--------------------')
    print(f'')
    return
    
def main(file):

    global instructions, reactor

    # Import input data
    parse_input_file(file)
    print(instructions)
    print(reactor)

    for c, i in enumerate(instructions):
        status, affected = i
        print(f'Step {c}...')
        for x in range(affected[0], affected[1] + 1):
            for y in range(affected[2], affected[3] + 1):
                for z in range(affected[4], affected[5] + 1):
                    reactor[x, y, z] = status
    
    # Cleanup
    print_reactor()
    print(f'Number of lit pixels: {lit()} (should be 590784)')
    print("Done!")


# main('tiniest.txt')
# main('tiny.txt')
# main('test.txt')
main('input.txt')
