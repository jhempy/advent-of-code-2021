# day16.py

def parse_input_file(file): 
    contents = ''
    f = open(file, "r")
    for line in f:
        contents = contents + line.rstrip('\n')
    f.close()
    return contents

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

def header(b):
    ver = int(b[0:3], 2)
    tid = int(b[3:6], 2)
    msg = b[6:]
    return ver, tid, msg

class packet:
    def __init__(self, contents):
        self.raw = contents
        self.version, self.typeid, self.parsed = parse_packet(self.raw)
        self.children = []
    def __str__(self):
        s = f'Packet: v={self.version}, typeid={self.typeid}, parsed={self.parsed}, children={len(self.children)}'
        return s

def parse_packet(packet):
    version, typeid, contents = header(packet)
    if (typeid == 4):
        # Message is a literal
        children = parse_literal(contents)
    else:
        # Message is an operator
        children = parse_operator(typeid, contents)
    return version, typeid, children


def parse_literal(msg):
    remaining_msg = ''
    decoded = ''
    flag = 1
    while flag > 0:
        flag = int(msg[0:1])
        decoded = decoded + msg[1:5]
        msg = msg[5:]
    if len(msg) > 10:
        remaining_msg = ''
    return int(decoded, 2), remaining_msg

def parse_operator(typeid, msg):
    ltid = msg[:1]
    msg = msg[1:]
    if ltid == '0':
        return operator_length(msg)
    if ltid == '1':
        return operator_subpackets(msg)

def operator_subpackets(msg):
    nos = int(msg[:11], 2)
    msg = msg[11:]
    return nos, msg

def operator_length(msg)
    sl = int(msg[:15], 2)
    msg = msg[sl:]
    if len(msg) > 10:

        return sl, msg
    return sl, ''


def main(file):

    # Prep data
    raw = parse_input_file(file)
    bstr = binary_from_hex(raw)

    root = packet(bstr)

    print(root)





    # Results and cleanup
    print('Done!')

# main('literal_2021.txt') 
main('operator_3packets.txt')
# main('operator_sum16.txt')
# main('operator_sum31.txt')
# main('literal_10_20.txt')
# main('operator_sum12.txt')
# main('operator_sum23.txt')
# main('test_3.txt')
# main('test_54.txt')
# main('test_7.txt')
# main('test_9.txt')
# main('test_lessthan_1.txt')
# main('test_greaterthan_0.txt')
# main('test_equal_0.txt')
# main('test_equal_1.txt')
# main('input.txt')
