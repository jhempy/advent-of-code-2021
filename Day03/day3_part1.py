# day3_part1.py

from collections import Counter

def get_bits(r):
    d = {}
    for i, c in enumerate(r):
        d[i] = int(c)
    return Counter(d)

def parse(file):
    lines = 0
    bit_counts = Counter()
    f = open(file, "r")
    for reading in f:
        lines = lines + 1
        reading_counter = get_bits(reading.strip())
        bit_counts = bit_counts + reading_counter
    f.close()
    return bit_counts, lines

def calculate_rates(file):
    gamma_binary = '';
    epsilon_binary = ''
    (bit_counts, line_count) = parse(file)
    for (bit, count) in sorted(bit_counts.items()):
        if (count > line_count/2):
            gamma_binary = gamma_binary + '1'
            epsilon_binary = epsilon_binary + '0'
        else:
            gamma_binary = gamma_binary + '0'
            epsilon_binary = epsilon_binary + '1'
    # print(gamma_binary)
    # print(epsilon_binary)
    return int(gamma_binary, 2), int(epsilon_binary, 2)


def calculate_power_consumption(file):
    (gamma_rate, epsilon_rate) = calculate_rates(file)
    return gamma_rate * epsilon_rate


def main(file):
    power_consumption = calculate_power_consumption(file)
    print(power_consumption)


def test():
    print(parse('101010'))

# test()
main('input.txt')
