# day20_part2.py

from collections import Counter

algorithm = ''
versions = []
padding = 100

def count_lit(image):
    lit = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == '#':
                lit = lit + 1
    return lit 

def enhance(image, iteration):
    global algorithm
    new_image = []
    for i, r in enumerate(image):
        temp = []
        for j, c in enumerate(image[i]):
            bstr = ''
            pstr = ''
            ns = neighbors(i, j)
            for n in ns:
                try:
                    pstr = pstr + image[n[0]][n[1]]
                except:
                    pstr = pstr + '.'
            bstr = map_pstr_to_bstr(pstr)
            pos = int(bstr, 2)
            new = algorithm[pos]
            # print(f'DEBUG: [{i},{j} -> {ns} -> {pstr} -> {bstr} -> {new}')
            temp.append(new)
        new_image.append(temp)
    return new_image

def map_pstr_to_bstr(pstr):
    bstr = ''
    for c in pstr:
        if c == '#':
            bstr = bstr + '1'
        else:
            bstr = bstr + '0'
    return bstr


def neighbors(r, c):
    n = []
    n.append([r-1, c-1])     # add neighbor to the nw
    n.append([r-1, c])       # add neighbor to the north
    n.append([r-1, c+1])     # add neighbor to the ne
    n.append([r, c-1])       # add neighbor to the west
    n.append([r, c])         # add self
    n.append([r, c+1])       # add neighbor to the east
    n.append([r+1, c-1])     # add neighbor to the se
    n.append([r+1, c])       # add neighbor to the south
    n.append([r+1, c+1])     # add neighbor to the sw
    return n

def trim_image(image, padding):
    smaller = []
    for r in image[padding:-padding]:
        smaller.append(r[padding:-padding])
    return(smaller)

def add_darkness_around_edges(image):
    global padding
    bigger = []
    new_cols = (padding * 2) + len(image[0])
    for p in range(padding):
        t = []
        for c in range(new_cols):
            t.append('.')
        bigger.append(t)
    for r in image:
        t = []
        for c in range(padding):
            t.append('.')
        t.extend(r)
        for c in range(padding):
            t.append('.')
        bigger.append(t)
    for p in range(padding):
        t = []
        for c in range(new_cols):
            t.append('.')
        bigger.append(t)
    return(bigger)

def parse_input_file(file): 
    global algorithm
    image = []
    f = open(file, "r")
    in_algorithm = True
    for (i, line) in enumerate(f):
        l = line.rstrip('\n')
        if l == '':
            # no longer in algorithm
            in_algorithm = False
        else:
            if in_algorithm:
                algorithm = algorithm + l
            else:
                image.append(list(l))
    f.close()
    versions.append(algorithm)
    return image

def print_image(printme):
    print(f'--------------------')
    print(f'INFO > print_image:')
    for i in printme:
        print(''.join(list(map(str, i))))
    print(f'--------------------')
    print(f'')
    return
    
def main(file):

    global versions, algorithm

    # Import input data
    image = parse_input_file(file)
    darkened = add_darkness_around_edges(image)
    versions.append(darkened)
    print(f'Number of lit pixels: {count_lit(image)}')

    iterations = 50
    for i in range(iterations):
        print(f'Enhancing...')
        image = versions[-1]
        # darkened = add_darkness_around_edges(image)
        # new = enhance(darkened)
        new = enhance(image, i)
        print(f'Number of lit pixels: {count_lit(new)}')
        versions.append(new)

    # Cleanup
    # last = trim_image(versions[-1], iterations)
    last = versions[-1]
    print_image(last)
    print(f'Number of lit pixels: {count_lit(last)}')
    print("Done!")

# main('test.txt')
main('input.txt')
