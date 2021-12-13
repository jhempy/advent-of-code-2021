# day12_part1.py

from collections import Counter

instructions = []

def parse_instruction(i):
    parts = i.split(' ')
    t = parts[2].split('=')
    return t[0], int(t[1])

def fold(dots, i):

    # fold the paper up (for horizontal y=... lines) 
    # or left (for vertical x=... lines
    
    t = []
    (d, loc) = parse_instruction(i)

    print(f'INFO: instruction: {i}')
    print(f'INFO: d = {d}')
    print(f'INFO: loc = {loc}')
    print('')


    if d == 'x':
        # fold vertically
        for y in dots:
            t.append(y[0:loc])        
        for r in range(len(t)):
            for i in range(loc):
                t[r][i] = t[r][i] + dots[r][len(dots[r])-1-i]


    elif d == 'y':
        # fold horizontally
        t = dots[0:loc]
        for i in range(loc):
            for c in range(len(t[0])):
                t[i][c] = t[i][c] + dots[len(dots)-1-i][c]

    return t

def parse_input_file(file): 
    global instructions
    dots = []
    temp = []
    xmax = 0
    ymax = 0
    f = open(file, "r")
    for line in f:
        if ',' in line:
            # this is a dot
            (x, y) = list(map(int, line.split(',')))
            xmax = max(x, xmax)
            ymax = max(y, ymax)
            temp.append([x, y])
        elif '=' in line:
            # this is a folding instruction
            instructions.append(line.rstrip('\n'))
    f.close()
    xmax = xmax + 1
    ymax = ymax + 1
    dots = make_grid(ymax, xmax)
    for (x, y) in temp:
        dots[y][x] = 1
    return dots

def make_grid(r, c):
    g = []
    for y in range(r):
        g.append([0] * (c))
    return g

def print_dots(dots):
    print(f'INFO: Dots:')
    for r in dots:
        t = list(map(lambda c : '#' if c else '.', r))
        print(''.join(t))
    print(f'INFO: Visible = {visible(dots)}')
    print(f'--------------------')
    print(f'')
    return

def visible(dots):
    total = 0
    for r in dots:
        for c in r:
            if c:
                total = total + 1
    return total

def main(file):

    global instructions

    # Import input data
    dots = parse_input_file(file)
    print_dots(dots)

    # Fold according to instructions
    while instructions:
        i = instructions.pop(0)
        dots = fold(dots, i)
        print_dots(dots)

    # Cleanup
    print("Done!")

main('input.txt')
