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
    else:
        # Message is an operator
        parse_operator(contents)
    return

def parse_literal(msg):
    print(f'  Parsing literal packet...')
    decoded = ''
    flag = 1
    while flag > 0:
        flag = int(msg[0:1])
        decoded = decoded + msg[1:5]
        msg = msg[5:]
    print(f'    {int(decoded, 2)}')
    if len(msg) > 10:
        packet_queue.append(msg)

def parse_operator(msg):
    print(f'  Parsing operator packet...')
    ltid = msg[:1]
    msg = msg[1:]
    if ltid == '0':
        # 15 bits
        operator_sub15(msg)
    if ltid == '1':
        # 11 bits
        operator_sub11(msg)

def operator_sub15(msg):
    sl = int(msg[:15], 2)
    print(f'    Parsing operator packet with a subpacket of length {sl}...')
    if sl == 0:
        print(f'LENGTH 0!')
        print(f'{msg}')
        print(f'{msg[15:]}')
    msg = msg[15:]
    packet_queue.append(msg[:sl])
    msg = msg[sl:]
    if len(msg) > 10:
        packet_queue.append(msg)

def operator_sub11(msg):
    nos = int(msg[:11], 2)
    msg = msg[11:]
    print(f'    Parsing operator packet with {nos} subpackets...')
    # for i in range(nos-1):
    #     print(f'      subpacket {i+1}')
    #     packet_queue.append(msg[:11])
    #     msg = msg[11:] 
    packet_queue.append(msg)

# def operator_sub11(msg):
#     nos = int(msg[:11], 2)
#     msg = msg[11:]
#     print(f'    Parsing operator packet with {nos} subpackets...')
#     for i in range(nos-1):
#         print(f'      subpacket {i+1}')
#         packet_queue.append(msg[:11])
#         msg = msg[11:] 
#     packet_queue.append(msg)

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
    bstr = binary_from_hex(raw)
    print(f'Raw is {raw}')
    print(f'Bstr is {bstr}')
    packet_queue.append(bstr)

    # Data contains nested packets
    # Parse recursively
    while len(packet_queue) > 0:
        print(f'---------------------------------------------------')
        print(f'Processing queue ({len(packet_queue)} packets)')
        print(f'{packet_queue}')
        print(f'Versions = {versions}')
        pkt = packet_queue.pop(0)
        parse_packet(pkt)

    # Cleanup
    print(f'Versions = {versions}')
    print(f'Sum = {sum(versions)}')
    print('Done!')


# main('literal_2021.txt') 
# main('operator_3packets.txt')
# main('operator_sum16.txt')
# main('operator_sum31.txt')
# main('literal_10_20.txt')
# main('operator_sum12.txt')
# main('operator_sum23.txt')
main('input.txt')
