# day19_part1.py

from collections import Counter

scanners = []
beacons = []

def parse_input_file(file): 
    global scanners
    f = open(file, "r")
    sid = 0 # id of current scanner
    bid = 0 
    for line in f:
        l = line.rstrip('\n')
        if l != '':
            if l[:3] == '---':
                # new scanner
                sid = l.split(' ')[2]
                scanners.append(scanner(sid))
            else:
                # beacon for the current scanner
                bid = bid + 1
                x, y, z = list(map(int, l.split(',')))
                beacons.append(beacon(bid, sid, x, y, z))

    f.close()
    return

class scanner:

    def __init__(self, id):
        self.id = id
        self.location = ''
        self.direction = ''
        self.beacons = []

    def __str__(self):
        out =       f'----------------' + '\n'
        out = out + f'Scanner {self.id}' + '\n'
        out = out + f'----------------' + '\n'
        return out

class beacon:

    def __init__(self, bid, sid, x, y, z):
        self.id = sid
        d = {'sid': sid, 'x': x, 'y': y, 'z': z}
        self.distances = []
        self.distances.append(d)
        self.neighbors = []

    def __str__(self):
        out =       f'----------------' + '\n'
        out = out + f'Beacon Object: {self.id}' + '\n'
        out = out + f'  Distances: {self.distances}' + '\n'
        out = out + f'----------------' + '\n'
        return out

def main(file):

    parse_input_file(file)


    for s in scanners:
        print(s)

    for b in beacons:
        print(b)


    # Cleanup
    print('')
    print('Done!')


main('test.txt')
# main('input.txt')

