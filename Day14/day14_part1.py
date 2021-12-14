# day14_part1.py

from collections import Counter

template = ''
rules = []

def insert():
    global template, rules
    t = ''
    for c in range(len(template)-1):
        t = t + template[c]
        for (p, ins) in rules:
            # print(f'c is {c}, pair is {p}, ins is {ins}')
            if p[0] == template[c] and p[1] == template[c+1]:
                # print('Match!')
                t = t + ins
                break
    t = t + template[-1]
    template = t

def parse_input_file(file): 
    global template, rules
    f = open(file, "r")
    for (i, line) in enumerate(f):
        if '->' in line:
            (pair, ins) = (line.rstrip('\n')).split(' -> ')
            rules.append([[pair[0], pair[1]], ins])
        if i == 0:
            template = line.rstrip('\n')

def main(file):

    global instructions

    # Import input data
    parse_input_file(file)
    print(template)
    print(rules)

    # Calculate insertions
    for x in range(10):
        print(f'x is {x}, length of template is {len(template)}')
        insert()
    # print(len(template))
    c = Counter(template)
    print(c)

    # Cleanup
    print("Done!")

main('test.txt')
