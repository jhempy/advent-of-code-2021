# day14_part2_2.py

from collections import Counter

pairs = Counter()
first = ''
last = ''
rules = {}

def increase():

    global pairs, first, last

    x = Counter()
    for t in pairs.keys():
        amount = pairs[t]

        # Update x
        (front, back) = rules[t]
        # print(f'for {t} add {amount} {front}')
        # print(f'for {t} add {amount} {back}')
        # print(f'for {t} remove {amount} {t}')
        x[front] = x[front] + amount
        x[back] = x[back] + amount

    # Update first and last
    first = rules[first][0]
    last = rules[last][1]

    print(f'  Summary of Step:')
    print(f'   pairs was {pairs}')
    print(f'        x is {x}')
    print(f'    first is {first}')
    print(f'     last is {last}')
    pairs = x
    print(f'    pairs is {pairs}')
    print(f'------------------------------')

def insert():
    global pairs, rules
    t = ''
    for c in range(len(pairs)-1):
        t = t + pairs[c]
        for (p, ins) in rules:
            # print(f'c is {c}, pair is {p}, ins is {ins}')
            if p[0] == pairs[c] and p[1] == pairs[c+1]:
                # print('Match!')
                t = t + ins
                break
    t = t + pairs[-1]
    pairs = t

def parse_input_file(file): 
    global pairs, rules, first, last
    f = open(file, "r")
    for (i, line) in enumerate(f):
        line = line.rstrip('\n')
        if '->' in line:
            (pair, ins) = line.split(' -> ')
            rules[pair] = [pair[0] + ins, ins + pair[1]]
        if i == 0:
            for i in range(len(line)-1):
                t = line[i:i+2]
                pairs[t] = pairs[t] + 1
            first = line[:2]
            last = line[-2:]

def main(file):

    global rules

    # Import input data
    parse_input_file(file)
    print(pairs)
    # print(rules)
    print(f'First is {first}')
    print(f'Last is {last}')
    print('')
    print('')

    # Calculate insertions
    steps = 10
    for x in range(steps):
        print(f'------------------------------')
        print(f'Interation: {x + 1}')
        increase()

    # Final calculation
    final = Counter()
    for t in pairs.keys():

        amount = pairs[t]
        
        print(f't is {t}, {amount}')

        front = t[0]
        back = t[1]

        print(f'front is {front}')
        print(f'back is {back}')

        final[front] = final[front] + amount
        if t == last:
            final[back] = final[back] + amount
        else:
            final[back] = final[back] - amount

        print(final)

    # print(f'Final is {final}')

    print(f'First is {first}')
    print(f'Last is  {last}')

    # Cleanup
    print("Done!")

main('test.txt')
