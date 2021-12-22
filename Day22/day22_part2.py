# day22_part2.py

from collections import Counter
import numpy as np

instructions = []
xmagic = 0
ymagic = 0
zmagic = 0
reactor = None

def lit():
    global magic, reactor
    lit = 0
    for x in range(0, magic):
        for y in range(0, magic):
            for z in range(0, magic):
                lit = lit + reactor[x,y,z]
    return int(lit)

def correct_boundaries(b):
    global xmagic, ymagic, zmagic
    c = []
    c.append(b[0] + xmagic)
    c.append(b[1] + xmagic)
    c.append(b[2] + ymagic)
    c.append(b[3] + ymagic)
    c.append(b[4] + zmagic)
    c.append(b[5] + zmagic)
    return c

def convert_coord(d, x):
    global xmagic, ymagic, zmagic
    if d == 'x':
        return int(x) + xmagic
    elif d == 'y':
        return int(x) + ymagic
    elif d == 'z':
        return int(x) + zmagic
    
def parse_input_file(file): 
    global instructions, xmagic, ymagic, zmagic, reactor
    
    # Max value pass
    xmin = 0
    ymin = 0
    zmin = 0
    f = open(file, "r")
    for line in f:
        l = line.rstrip('\n')
        status, temp = l.split(' ')
        ranges = temp.split(',')
        boundaries = []
        for r in ranges:
            d, b = r.split('=')
            b = b.split('..')
            if d == 'x':
                xmin = int(b[0]) if int(b[0]) < xmin else xmin
            if d == 'y':
                ymin = int(b[0]) if int(b[0]) < ymin else zmin
            if d == 'z':
                zmin = int(b[0]) if int(b[0]) < zmin else zmin
    xmagic = 0 if xmin > 0 else abs(xmin)
    ymagic = 0 if ymin > 0 else abs(ymin)
    zmagic = 0 if zmin > 0 else abs(zmin)
    f.close()

    # Fix reactor
    reactor = np.zeros([xmagic, ymagic, zmagic], bool) # to represent -50..50 in each axis

    # Import pass
    f = open(file, "r")
    for line in f:
        l = line.rstrip('\n')
        status, temp = l.split(' ')
        ranges = temp.split(',')
        boundaries = []
        for r in ranges:
            d, b = r.split('=')
            b = b.split('..')
            boundaries.append(convert_coord(d, b[0]))
            boundaries.append(convert_coord(d, b[1]))
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
main('tiny.txt')
# main('test.txt')
# main('new_test.txt')
# main('input.txt')
