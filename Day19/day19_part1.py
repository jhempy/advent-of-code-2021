# day19_part1.py

from collections import Counter

def parse_input_file(file): 
    f = open(file, "r")
    for line in f:
        l = line.rstrip('\n')
        if l != '':
            if l[:3] == '---':
                # new scanner
                id = l.split(' ')[2]


                print(id)



    f.close()
    return

class scanner:

    def __init__(self, id):
        self.id = id
        self.beacons = []

    def __str__(self):
        out =       f'----------------' + '\n'
        out = out + f'Scanner Object: {self.id}' + '\n'
        out = out + f'----------------' + '\n'
        return out

class beacon:

    def __init__(self, id):
        self.id = id

    def __str__(self):
        out =       f'----------------' + '\n'
        out = out + f'Beacon Object: {self.id}' + '\n'
        out = out + f'----------------' + '\n'
        return out



def main(file):

    parse_input_file(file)


    # Cleanup
    print('')
    print('Done!')


main('test.txt')
# main('input.txt')
