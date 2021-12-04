# day3_part1.py

from collections import Counter

def parse(r):
    d = {}
    for i, c in enumerate(r):
        d[i] = int(c)
    return Counter(d)

def count_bits(file):
    lines = 0

    bit_counts = Counter()

    f = open(file, "r")
    for reading in f:
        lines = lines + 1
        reading_counter = parse(reading.strip())
        bit_counts = bit_counts + reading_counter

    f.close()
    return bit_counts

def calculate_rates(file):
    bit_counts = count_bits(file)

    print(sorted(bit_counts.items()))
    return 1,2


def calculate_power_consumption(file):
    (gamma_rate, epsilon_rate) = calculate_rates(file)
    return gamma_rate * epsilon_rate


def main(file):
    power_consumption = calculate_power_consumption(file)
    print(power_consumption)


def test():
    print(parse('101010'))

# test()
main('test.txt')
