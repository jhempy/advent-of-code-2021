# day16_part2_2.py

def operate(operations, literals):

    print(f'---------------------------')
    print(f'OPERATING!')
    print(f'operations = {operations}')
    print(f'literals = {literals}')

    sublits = []

    for (i, o) in enumerate(reversed(operations)):
        print(f'{i}: processing {o}')
        print(f'Literals are {literals}')

        typeid = o[0]
        lits = -o[1]

        result = 0

        if (typeid == 0):
            # Sum packet
            print(f'  Sum {lits} literals')
            t = 0
            xs = literals[lits:]
            print(f'{xs}')
            literals = literals[:lits]
            for x in xs:
                t = t + x
            result = t

        elif (typeid == 1):
            # Product packet
            print(f'  Multiply {lits} literals')
            xs = literals[lits:]
            print(f'{xs}')
            literals = literals[:lits]
            t = 1
            for x in xs:
                t = t * x
            result = t

        elif (typeid == 2):
            # Minimum packet
            print(f'  Minimum {lits} literals')
            xs = literals[lits:]
            print(f'{xs}')
            literals = literals[:lits]
            result = min(xs)

        elif (typeid == 3):
            # Maximum packet
            print(f'  Maximum {lits} literals')
            xs = literals[lits:]
            print(f'{xs}')
            literals = literals[:lits]
            result = max(xs)

        elif (typeid == 5):
            # Greater-than packet
            print(f'  Greater than {lits} literals')
            xs = literals[lits:]
            print(f'{xs}')
            literals = literals[:lits]
            result = int(xs[0] > xs[1])

        elif (typeid == 6):
            # Less-than packet
            print(f'  Less than {lits} literals')
            xs = literals[lits:]
            print(f'{xs}')
            literals = literals[:lits]
            result = int(xs[0] < xs[1])

        elif (typeid == 7):
            # Equal-to packet
            print(f'  Equal to {lits} literals')
            xs = literals[lits:]
            print(f'{xs}')
            literals = literals[:lits]
            result = int(xs[0] == xs[1])

        sublits.append(result)

    return sublits

def start_queue(msg):
    queue = []
    versions = []
    operations = []
    literals = []
    queue.append(msg)
    while len(queue) > 0:
        print(f'---------------------------------------------------')
        packet = queue.pop(0)
        parse_packet(queue, versions, operations, literals, packet)
    return versions, operations, literals

def operator_sub15(queue, versions, operations, literals, typeid, msg):
    subpacket_length = int(msg[:15], 2)
    msg = msg[15:]
    print(f'    Parsing operator packet with a subpacket of length {subpacket_length}...')
    print(f'    Reducing...')

    # Spin off new queue
    subvers, subops, sublits = start_queue(msg[:subpacket_length])
    versions.extend(subvers)

    print(f'')
    print(f'Subvers: {subvers}')
    print(f'Subops:  {subops}')
    print(f'Sublits: {sublits}')

    # if len(subops) > 0:
    #     sublits = operate(subops, sublits)

    operations.append([typeid, len(sublits)])
    operations.extend(subops)
    literals.extend(sublits)
    
    msg = msg[subpacket_length:]
    if len(msg) > 10:
        queue.append(msg)

def operator_sub11(queue, versions, operations, literals, typeid, msg):
    nos = int(msg[:11], 2)
    msg = msg[11:]
    print(f'    Parsing operator packet with {nos} subpackets...')
    operations.append([typeid, nos])
    queue.append(msg)

def parse_operator(queue, versions, operations, literals, typeid, msg):
    print(f'  Parsing operator packet...')
    ltid = msg[:1]
    msg = msg[1:]
    if ltid == '0':
        # 15 bits
        operator_sub15(queue, versions, operations, literals, typeid, msg)
    if ltid == '1':
        # 11 bits
        operator_sub11(queue, versions, operations, literals, typeid, msg)

def parse_literal(queue, versions, operations, literals, msg):
    print(f'  Parsing literal packet...')
    decoded = ''
    flag = 1
    while flag > 0:
        flag = int(msg[0:1])
        decoded = decoded + msg[1:5]
        msg = msg[5:]
    literals.append(int(decoded, 2))
    if len(msg) > 10:
        queue.append(msg)

def parse_packet(queue, versions, operations, literals, packet):

    print(f'Parsing packet...')

    # Check the package header
    version, typeid, contents = header(packet)
    versions.append(version)

    # Continue based on typeid
    if (typeid == 4):
        # Message is a literal
        parse_literal(queue, versions, operations, literals, contents)
    else:
        # Message is an operator
        parse_operator(queue, versions, operations, literals, typeid, contents)
    return

def header(b):
    ver = int(b[0:3], 2)
    tid = int(b[3:6], 2)
    msg = b[6:]
    return ver, tid, msg

def binary_from_hex(h):
    codes = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'    
    }
    b = ''
    for c in h:
        b = b + codes[c]
    return b

def parse_input_file(file): 
    contents = ''
    f = open(file, "r")
    for line in f:
        contents = contents + line.rstrip('\n')
    f.close()
    return contents

def main(file):

    # Prep data
    raw = parse_input_file(file)
    bstr = binary_from_hex(raw)

    versions, operations, literals = start_queue(bstr)

    # Get ready for awesome
    print(f'Operations = {operations}')
    print(f'Literals = {literals}')
    print(f'')

    # Calculate result
    result = operate(operations, literals)
    print(f'Result = {result}')


    print('Done!')


# main('test_3.txt')
# main('test_54.txt')
# main('test_7.txt')
# main('test_9.txt')
# main('test_lessthan_1.txt')
# main('test_greaterthan_0.txt')
# main('test_equal_0.txt')
# main('test_equal_1.txt')
main('input.txt')
