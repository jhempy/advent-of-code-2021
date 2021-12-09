# day8_part1.py

from collections import Counter

def count_ssd_lengths(displays):
	lengths = Counter()
	for d in displays:
		for ssd in d[1]:
			lengths.update([len(ssd)])
	return lengths

def parse_input_file(file): 

	# Each entry consists of ten unique signal patterns, a | delimiter, 
	# and finally the four digit output value. Within an entry, the same 
	# wire/segment connections are used (but you don't know what the 
	# connections actually are). The unique signal patterns correspond 
	# to the ten different ways the submarine tries to render a digit 
	# using the current wire/segment connections.

	displays = []
	f = open(file, "r")
	for line in f:
		(combo_string, ssd_string) = line.split('|')
		combos = combo_string.split()
		ssds = ssd_string.split()
		displays.append([combos, ssds])
	f.close()
	return displays

def main(file):
	print("Starting...")
	displays = parse_input_file(file)
	# print(f"Input data: {displays}")

	# Count codes corresponding to 1, 4, 7, 8
	ssd_lengths = count_ssd_lengths(displays)

	print(ssd_lengths)

	# 0 uses 6 segments
	# 1 uses 2 segments ***
	# 2 uses 5 segments
	# 3 uses 5 segments
	# 4 uses 4 segments ***
	# 5 uses 5 segments
	# 6 uses 6 segments
	# 7 uses 3 segments *** 
	# 8 uses 7 segments ***
	# 9 uses 5 segments

	uniques = ssd_lengths[2] + ssd_lengths[4] + ssd_lengths[3] + ssd_lengths[7]

	print("Uniques: ", uniques)





	print("Done!")

main('input.txt')
