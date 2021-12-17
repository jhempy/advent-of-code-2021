# day16_part1.py

packet_queue = []
versions = []

def parse_packet(pkt):
    print(f'Parsing packet...')
    global versions
    ver, typeid, contents = header(pkt)
    versions.append(ver)

    # Continue based on typeid
    if (typeid == 4):
        # Message is a literal
        decoded = parse_literal(contents)
        # print(f'Literal decodes to: {decoded}')        
    else:
        # Message is an operator
        parse_operator(contents)
    return

def parse_literal(packet):
    print(f'  Parsing literal packet...')
    decoded = ''
    flag = 1
    while flag > 0:
        flag = int(packet[0:1])
        decoded = decoded + packet[1:5]
        packet = packet[5:]
    return int(decoded, 2)

def parse_operator(msg):
    print(f'  Parsing operator packet...')
    ltid = msg[0:1]
    if ltid == '0':
        # 15 bits
        operator_sub15(msg[1:])
    if ltid == '1':
        # 11 bits
        operator_sub11(msg[1:])

def operator_sub15(msg):
    print(f'    Parsing operator packet (length 15 type)...')
    sl = int(msg[1:16], 2)
    packet_queue.append(msg[:sl]) # break out this subpacket
    if msg: 
        packet_queue.append(msg[sl:]) # remainer is more packets


def operator_sub11(msg):
    nos = int(msg[1:12], 2)
    print(f'    Parsing operator packet (length 11 type)...')
    for i in range(nos):
        print(f'      {i} packet')
        packet_queue.append(msg[:11]) # append a packet
        msg = msg[11:]
    if msg:
        packet_queue.append(msg) # remainder might be more packets

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

    global packet_queue

    # Prep data
    raw = parse_input_file(file)
    all = binary_from_hex(raw)
    packet_queue.append(all)

    # Data contains nested packets
    # Parse recursively
    while len(packet_queue) > 0:
        pkt = packet_queue.pop(0)
        parse_packet(pkt)

    # Cleanup
    print(f'Versions = {versions}')
    print(f'Sum = {sum(versions)}')
    print('Done!')


# main('literal_2021.txt')
main('operator_sum16.txt')
# main('operator_sum12.txt')
# main('operator_sum23.txt')
# main('operator_sum31.txt')