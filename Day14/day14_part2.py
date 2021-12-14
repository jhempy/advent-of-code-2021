# day14_part1.py

from collections import Counter

template = ''
rules = {}

def insert():
    global template, rules
    old = template
    new = ''
    while len(old) > 0:
        ks = list(rules.keys())
        ks.sort(key=lambda item: (-len(item), item))
        changed = False
        for k in ks:
            if old.startswith(k):
                t = rules[k]
                new = new + t[:-1]
                old = old[len(k)-1:]
                changed = True
                break
        if (not changed):
            new = new + old[:1]
            old = old[1:]
    new = new + old
    rules[template] = new
    template = new

def parse_input_file(file): 
    global template, rules
    f = open(file, "r")
    for (i, line) in enumerate(f):
        if '->' in line:
            (pair, ins) = (line.rstrip('\n')).split(' -> ')
            rules[pair] = pair[0] + ins + pair[1]
        if i == 0:
            template = line.rstrip('\n')

def main(file):

    global instructions

    # Import input data
    parse_input_file(file)
    print(template)
    print(rules)

    # Calculate insertions
    for x in range(40):
        print(f'x is {x}, length of template is {len(template)}')
        insert()
    # print(len(template))
    c = Counter(template)
    print(c)

    # Cleanup
    print("Done!")

main('input.txt')
