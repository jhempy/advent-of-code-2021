# Day 18: Snailfish (part 1)

import re
import math
from collections import Counter

def explode(sfnum):

    # To explode a pair, the pair's left value is added to the first regular 
    # number to the left of the exploding pair (if any), and the pair's right 
    # value is added to the first regular number to the right of the exploding 
    # pair (if any). Exploding pairs will always consist of two regular numbers. 
    # Then, the entire exploding pair is replaced with the regular number 0.

    txt = f'{sfnum}'
    result = txt
    pattern = "(\[\d+, \d+\])"
    matches = re.finditer(pattern, txt)
    deep_matches = 0

    for m in matches:
        l = int(eval(m.group())[0])
        r = int(eval(m.group())[1])
        left = txt[:m.span()[0]]
        right = txt[m.span()[1]:]
        c = Counter(txt[:m.span()[0]])
        depth = c['['] - c[']']
        # print(f'depth is {depth}')
        if deep_matches == 0 and depth > 3:

            deep_matches = deep_matches + 1

            # Is there a digit immediately left of the match?
            n = re.finditer("\d+", left)
            x = None
            for x in n:
                pass    
            if x is not None:
                # x is now the rightmost left match
                new = str(int(left[x.span()[0]:x.span()[1]]) + l)
                left = left[:x.span()[0]] + new + left[x.span()[1]:]
            else:
                # left = left + '0'
                pass

            # Is there a digit immediately right of the match?
            x = re.search("\d+", right)
            if x:
                temp = int(right[x.span()[0]:x.span()[1]])
                new = str(temp + r)
                right = right[:x.span()[0]] + new + right[x.span()[1]:]
            else:
                # right = '0' + right
                pass
            if (left[-2] == ',' or right[:2] == ', '):
                result = left + '0' + right
            else:
                result = left + right
            
        else:
            # The pair isn't deep enough
            pass

    return result

def split(sfnum):

    # To split a regular number, replace it with a pair; the left element of 
    # the pair should be the regular number divided by two and rounded down, 
    # while the right element of the pair should be the regular number divided 
    # by two and rounded up.

    txt = f'{sfnum}'
    pattern = "(\d\d+)"
    match = re.search(pattern, txt)
    if match:
        match_start = match.span()[0]
        match_end = match.span()[1]
        x = int(match.group())
        new = f'[{math.floor(x/2)}, {math.ceil(x/2)}]'
        txt = txt[:match_start] + new + txt[match_end:]
    return txt

def reduce(sfnum):
    print(f'------------------------')
    print(f'after addition:  {sfnum}')

    ecount = 1
    keep_exploding = True
    scount = 1
    working = str(sfnum)

    while (ecount or scount):
        ecount = 0
        scount = 0
        keep_exploding = True

        # Explode as much as possible
        while keep_exploding:
            last = working
            working = explode(working)
            # print(f'after explode:   {working}')
            if last != working:
                # explode did something
                print(f'after explode:   {working}')
                ecount = ecount + 1
            else:
                keep_exploding = False

        # Split at most once
        last = working
        working = split(working)
        # print(f'after split:     {working}')
        if last != working:
            # split did something
            print(f'after split:     {working}')
            scount = scount + 1

    print(f'reduction:       {working}')
    print(f'------------------------')
    return working

def magnitude(sfnum):
    e = ''
    next_digit_close_parens = False
    for i, c in enumerate(sfnum):
        if c == '[':
            e = e + '('
        if c == ']':
            e = e + ')'
        if c in list(map(str, range(10))):
            e = e + c
            if next_digit_close_parens:
                e = e + ')'
                next_digit_close_parens = False
        if c == ' ':
            pass
        if c == ',':
            if sfnum[i-1:i+1] == '],':
                e = e + '*3+2*'
            elif sfnum[i:i+3] == ', [':
                e = e + '+'
            else:
                e = e[:-1] + '(' + e[-1] + '*3)+(2*'
                next_digit_close_parens = True
        # print(c)
        # print(e)

    return eval(e)

def parse_input_file(file): 
    numbers = []
    f = open(file, "r")
    for line in f:
        line = line.rstrip('\n')
        numbers.append(line)
    f.close()
    return numbers

def main(file):

    # Prep data
    numbers = parse_input_file(file)
    print(numbers)

    # r = split(numbers[0])
    # r = explode(numbers[0])
    # r = reduce(numbers[0])
    # print(r)

    # Perform addition
    while len(numbers) > 1:
        first = eval(numbers.pop(0))
        second = eval(numbers.pop(0))
        numbers.insert(0, str(reduce([first, second])))

    # Cleanup
    print('')
    print('')
    print(numbers)
    print('')
    print(f'Magnitude is {magnitude(numbers[0])}')
    print('')
    print('Done!')


# main('mag_143.txt')
# main('mag_1384.txt')
# main('explode.txt')
# main('split.txt')
# main('tiny.txt')
# main('test.txt')
# main('input.txt')
main('dave1.txt')
