# day15_part2.py

from collections import Counter

roof = []
dests = []

class dest:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.risk_of = roof[self.row][self.col]
        self.risk_to = 0
    def __str__(self):
        s = '[' + str(self.row) + ',' + str(self.col) + '], risk_of=' + str(self.risk_of) + ', risk_to=' + str(self.risk_to)
        return s
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col  
    def __key__(self):
        return self.row, self.col      

def neighbors(d):
    global roof, dests
    r = d.row
    c = d.col
    global roof
    t = []
    n = []
    # t.append([r-1, c-1])     # add neighbor to the nw
    t.append([r-1, c])       # add neighbor to the north
    # t.append([r-1, c+1])     # add neighbor to the ne
    t.append([r, c+1])       # add neighbor to the east
    t.append([r, c-1])       # add neighbor to the west
    # t.append([r+1, c+1])     # add neighbor to the se
    t.append([r+1, c])       # add neighbor to the south
    # t.append([r+1, c-1])     # add neighbor to the sw
    for (tr, tc) in t:
        if tr in range(len(roof)) and tc in range(len(roof[0])):
            n.append(dest(tr, tc))
    return n

def parse_input_file(file): 
    global roof, end
    f = open(file, "r")
    for (i, line) in enumerate(f):
        l = line.rstrip('\n')
        roof.append(list(map(int, list(l))))
        end = [i, len(l)-1]
    f.close()
    embiggen()
    return

def embiggen():
    global roof
    biggen = roof.copy()
    temp = roof.copy()
    for i in range(4):
        print(f'increasing columns {i}')
        for j in range(len(temp)):
            temp[j] = list(map(advance, temp[j]))
            biggen[j].extend(temp[j])
    temp = biggen.copy()
    for i in range(4):
        print(f'increasing rows {i}')
        for j in range(len(temp)):
            temp[j] = list(map(advance, temp[j]))
            biggen.append(temp[j])
    print(biggen)
    roof = biggen
    return


def advance(x):
    if x + 1 == 10:
        return 1
    else:
        return x + 1

def print_roof():
    global roof
    print(f'--------------------')
    print(f'INFO > Roof:')
    for r in roof:
        print(''.join(list(map(str, r))))
    print(f'--------------------')
    print(f'')
    return

def print_dests():
    global dests
    print(f'--------------------')
    print(f'INFO > Destinations:')
    print_list_of_dests(dests)
    print(f'--------------------')
    return

def print_list_of_dests(ds):
    for d in ds:
        print(d)
    return
    
def main(file):

    global roof, dests

    # Import input data
    parse_input_file(file)
    print_roof()

    # First iteration
    start = dest(0, 0)
    dests.append(start)

    delta = 100
    last = 100
    loops = 0

    while delta != 0:

        loops = loops + 1

        # Loop
        for i in range( len(roof) + len(roof[0]) - 1):
        # for i in range(3):

            print(f'loops = {loops}, i = {i}, delta = {delta}')

            # Find all points on roof where r + c = i
            current = []
            for r in range(i+1):
                try:
                    current.append(dest(r, i-r))
                except:
                    pass

            # print_list_of_dests(current)

            for c in current:

                useme = c

                oldc = next((x for x in dests if x.row == useme.row and x.col == useme.col), None)
                if oldc:
                    useme = oldc
                    # print(f'  We have already seen this CURRENT: {useme}')
                else:
                    # print(f'  This is a new CURRENT: {useme}')
                    pass

                for n in neighbors(useme):

                    # Have we seen this neighbor before?
                    existing = next((x for x in dests if x.row == n.row and x.col == n.col), None)
                    if existing:
                        # print(f'  We have already seen {existing}')
                        if n == start:
                            # print(f'  Can\'t go back to start')
                            pass
                        else:
                            weight = useme.risk_to + existing.risk_of
                            # print(f'  c.risk_to = {useme.risk_to}')
                            # print(f'  x.risk_of = {existing.risk_of}')
                            # print(f'  weight    = {weight}')
                            if existing.risk_to < weight:
                                # print('  -- been here before, and less riskily')
                                pass
                            elif existing.risk_to == weight:
                                # print('  -- been here before, same risk')
                                pass
                            elif existing.risk_to > weight:
                                # print('  -- been here before, but more riskily -- updating')
                                existing.risk_to = weight

                    else:
                        weight = useme.risk_to + n.risk_of
                        n.risk_to = weight
                        # print(f'  New destination {n}, weight={weight}')
                        dests.append(n)

        end = next((x for x in dests if x.row == useme.row and x.col == useme.col), None)
        delta = last - end.risk_to
        print(f'Delta is {delta}')
        last = end.risk_to


    # What happened?
    print_dests()
    print(f'Delta is {delta} after {loops} loops')


    # Cleanup
    print_roof()
    print(f'roof rows = {len(roof)}, roof cols = {len(roof[0])} ')
    print("Done!")

# main('tiniest.txt')
# main('tinier.txt')
# main('tiny.txt')
# main('test.txt')
main('input.txt')
# main('testx5.txt')
