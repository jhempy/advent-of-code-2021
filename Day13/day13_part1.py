# day12_part1.py

from collections import Counter

instructions = []

def parse_instruction(i):
    return ('', '')

def fold(dots, i):
    # fold the paper up (for horizontal y=... lines) 
    # or left (for vertical x=... lines
    (direction, index) = parse_instruction(i)
    return dots

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
    for y in range(ymax):
        dots.append([0] * xmax)
    for (x, y) in temp:
        dots[y][x] = 1
    return dots

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
            total = total + c
    return total
def main(file):

    global instructions

    # Import input data
    dots = parse_input_file(file)
    print_dots(dots)

    # Fold according to instructions
    for i in instructions:
        dots = fold(dots, i)
        print_dots(dots)

    # Cleanup
    print("Done!")

main('test.txt')
