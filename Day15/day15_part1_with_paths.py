# day15_part1.py

from collections import Counter

start = [0,0]
roof = []
end = []
paths = []
discarded = []
plums = []
risks = []
lowest = 0

def save_state():
    global paths
    with open('paths.txt', 'w') as f:
        for p in paths:
            f.write("%s\n" % p)
    f.close()
    print(f'INFO > paths saved')
    return

def extreme_paths():
    global paths
    s = sorted(paths, key=lambda p: len(p))
    if s:
        print(f'INFO > shortest path length = {len(s[0])}')
        print(f'INFO > longest path length = {len(s[-1])}')
    else:
        print(f'INFO > s is {s}')
    return

def risk(p):
    global roof
    r = 0
    for x in p[1:]: # we don't count start in the risk
        r = r + roof[x[0]][x[1]]
    return r

def calculate_risks():
    global plums, risks
    for p in plums:
        risks.append(risk(p))
    return

def calculate_paths():
    print(f'Calculating paths...')

    global paths, roof, start, end

    # Seed paths with the only valid starting combinations
    start_paths()
    print_paths()

    while paths:
        new = []
        for p in paths:
            ns = find_next(p)
            for n in ns:
                t = p.copy()
                t.append(n)
                new.append(t)
        paths = prune_paths(new)
        extreme_paths()
        print_counts()
        save_state()

    print(f'Recursion done! Yay!')
    print(f'--------------------')
    print(f'')
    return

def prune_paths(new):
    global roof, plums, end, lowest
    r = []
    ended = 0
    higher_risk = 0
    print(f'INFO (prune) > new paths to consider = {len(new)}')
    print(f'INFO (prune) > lowest = {lowest}')
    for n in new:
        t = risk(n)
        if t > lowest:
            higher_risk = higher_risk + 1
        elif n[-1] == end:
            print(f'INFO (prune) > path ended {n}, risk is {t}, lowest is {lowest}') 
            if t <= lowest:
                lowest = t
                print(f'INFO (prune) > new lowest risk = {lowest}')
                plums.append(n)
            else:
                print(f'INFO (prune) > path ended but not lower {n}') 
                ended = ended + 1
        else:
            r.append(n)
    print(f'INFO (prune) > ended not lower = {ended}, higher risk = {higher_risk}')
    print(f'INFO (prune) > remaining new paths = {len(r)}')
    return r

def find_next(prev):
    global roof
    t = []
    n = []
    (r, c) = prev[-1]
    # t.append([r-1, c-1])     # add neighbor to the nw
    t.append([r-1, c])       # add neighbor to the north
    # t.append([r-1, c+1])     # add neighbor to the ne
    t.append([r, c+1])       # add neighbor to the east
    t.append([r, c-1])       # add neighbor to the west
    # t.append([r+1, c+1])     # add neighbor to the se
    t.append([r+1, c])       # add neighbor to the south
    # t.append([r+1, c-1])     # add neighbor to the sw
    for (tr, tc) in t:
        # only add neighbors we haven't visited yet
        if tr in range(len(roof)) and tc in range(len(roof[0])):
            if [tr, tc] not in prev: 
                n.append([tr, tc])
            else:
                # print(f'Excluding backtracking!')
                pass
    # sort n by risk
    s = sorted(n, key=lambda n: roof[n[0]][n[1]])
    # print(f'sorted = {s}')

    # return at_most n
    # m = s[:at_most]
    # print(f'at most = {m}')
    return s

def add_red_herring():
    global roof, paths, lowest
    rh = []
    # add first column
    for r in range(len(roof)-1):
        rh.append([r, 0])
    # add final row
    for c in range(len(roof[r])):
        rh.append([len(roof)-1, c])

    print(f'Red herring is {rh}')
    lowest = risk(rh)
    print(f'Lowest is {lowest}')
    plums.append(rh)
    return

def start_paths():
    global roof, paths, start
    neighbors = [[0,1], [1,0]]
    for n in neighbors:
        paths.append([start, n])
    return

def parse_input_file(file): 
    global roof, end, lowest
    f = open(file, "r")
    for (i, line) in enumerate(f):
        l = line.rstrip('\n')
        roof.append(list(map(int, list(l))))
        end = [i, len(l)-1]
    f.close()
    add_red_herring()
    print_plums()
    return

def print_roof():
    global roof, start, end
    print(f'--------------------')
    print(f'INFO > Start: {start} -> {roof[start[0]][start[1]]}')
    print(f'INFO > End: {end} -> {roof[end[0]][end[1]]}')
    print(f'INFO > Roof:')
    # print(f'{roof}')
    for r in roof:
        print(''.join(list(map(str, r))))
    print(f'--------------------')
    print(f'')
    return

def print_paths():
    global paths
    print(f'INFO > Paths:')
    for p in paths:
        print(p)
    print(f'--------------------')
    print(f'')
    return

def print_plums():
    global plums
    print(f'INFO > Plums:')
    for p in plums:
        print(p)
    print(f'--------------------')
    print(f'')
    return

def print_counts():
    print(f'INFO > len(paths) is {len(paths)}')    
    print(f'INFO > len(plums) is {len(plums)}')    
    print(f'--------------------')

def main(file):

    global paths, risks

    # Import input data
    parse_input_file(file)
    print_roof()

    # cheat a little
    lowest = 532

    # Calculate paths
    calculate_paths()

    # Calculate risks
    calculate_risks()

    # Cleanup
    print(f'Number of paths: {len(paths)}')
    print(f'Risks: {risks}')
    print(f'Smallest risk: {min(risks)}')
    print("Done!")

# main('tiniest.txt')
# main('tinier.txt')
# main('tiny.txt')
# main('test.txt')
main('input.txt')
