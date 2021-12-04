# day3_part2.py

from collections import Counter

def get_bits(r):
    d = {}
    for i, c in enumerate(r):
        d[i] = int(c)
    return Counter(d)

def parse(readings):
    bit_counts = Counter()
    for reading in readings:
        reading_counter = get_bits(reading.strip())
        bit_counts = bit_counts + reading_counter
    return bit_counts

def slurp(file):
    readings = []
    f = open(file, "r")
    for reading in f:
        readings.append(reading.strip())
    f.close()
    return readings


def keep_most_common(readings, position):
	if (len(readings) == 1):
		return readings[0]
	else:
		bit_counts = parse(readings)
		target = 1 if (bit_counts[position] >= len(readings)/2) else 0
		temp = list(filter(lambda x: int(x[position]) == target, readings))
		return keep_most_common(temp, position + 1)


def keep_least_common(readings, position):
	if (len(readings) == 1):
		return readings[0]
	else:
		bit_counts = parse(readings)
		target = 0 if (bit_counts[position] >= len(readings)/2) else 1
		temp = list(filter(lambda x: int(x[position]) == target, readings))
		return keep_least_common(temp, position + 1)


def calculate_oxygen_rating(file):
	readings = slurp(file)
	oxygen_rating = keep_most_common(readings, 0)
	return int(oxygen_rating, 2)


def calculate_co2_rating(file):
	readings = slurp(file)
	co2_rating = keep_least_common(readings, 0)
	return int(co2_rating, 2)


def calculate_life_support_rating(file):
    oxygen_rating = calculate_oxygen_rating(file)
    co2_rating = calculate_co2_rating(file)
    return oxygen_rating * co2_rating

def main(file):
    life_support_rating = calculate_life_support_rating(file)
    print(life_support_rating)

main('input.txt')

