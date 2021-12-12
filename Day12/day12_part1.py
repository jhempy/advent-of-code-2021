# day12_part1.py

from collections import Counter

paths = []
caves = {}
inputs = []

def calculate_paths():
    print(f'Calculating paths...')

    global paths, caves, inputs

    # Seed paths with the only valid starting combinations
    start_paths()
    print_paths()

    # Create temporary variable for updated paths
    while not all_ended():
        paths = prune(extend_paths())

    print(f'Recursion done! Yay!')
    print(f'--------------------')
    print(f'')
    return

def all_ended():
    global paths
    all_ended = True
    for p in paths:
        if p[-1] != 'end':
            all_ended = False
    return all_ended

def extend_paths():
    global caves, paths
    temp = []
    for p in paths:
        try:
            for n in caves[p[-1]]:
                next = p.copy()
                next.append(n)
                temp.append(next)
        except KeyError:
            temp.append(p)

    return temp

def prune(plums):
    print('')
    print('')
    print('')
    temp = []
    for p in plums:
        keeper = True # assume it's a valid path
        c = Counter(p)
        for cave, count in c.items():
            # print(f'Cave is {cave}, count is {count}')
            if (cave == cave.lower()) and (count > 1):
                # uh oh, bad path
                keeper = False
                # print(f'  toss out {p}')
        if keeper:
            temp.append(p)
    # print(f'Temp is {temp}')
    return temp

def start_paths():
    for pos in caves['start']:
        paths.append(['start', pos])
    return

def connect_caves():
    global caves
    for (b, e) in inputs:
        # b -> e
        if b != 'end': 
            try:
                caves[b].append(e)
            except KeyError:
                caves[b] = []
                caves[b].append(e)
        # e -> b
        if e != 'end': 
            try: 
                caves[e].append(b)
            except KeyError:
                caves[e] = []
                caves[e].append(b)

def parse_input_file(file): 
    f = open(file, "r")
    for line in f:
        inputs.append(line.rstrip('\n').split('-'))
    f.close()
    return

def print_caves():
    print(f'INFO: Cave data:')
    for c in caves:
        print(f'{c} -> {caves[c]}')
    print(f'--------------------')
    print(f'')
    return

def print_input():
    print(f'INFO: Input data:')
    for i in inputs:
        print(i)
    print(f'--------------------')
    print(f'')
    return

def print_paths():
    print(f'INFO: Paths:')
    for p in paths:
        print(p)
    print(f'--------------------')
    print(f'')
    return

def main(file):

    # Import input data
    parse_input_file(file)
    print_input()

    # Connect caves
    connect_caves()
    print_caves()

    # Calculate paths
    calculate_paths()
    print_paths()

    # Cleanup
    print(f'Number of paths: {len(paths)}')
    print("Done!")

main('input.txt')
