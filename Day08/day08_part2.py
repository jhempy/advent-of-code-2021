# day8_part2.py

from collections import Counter

# All
# ---------------
# 0 | abc efg | 6
# 1 |   c  f  | 2
# 2 | a cde g | 5
# 3 | a cd fg | 5 
# 4 |  bcd f  | 4
# 5 | ab d fg | 5
# 6 | ab defg | 6
# 7 | a c  f  | 3
# 8 | abcdefg | 7
# 9 | abcd fg | 6

# Uniques
# ---------------
# 1 |   c  f  | 2
# 4 |  bcd f  | 4
# 7 | a c  f  | 3
# 8 | abcdefg | 7

# Fives
# ---------------
# 2 | a cde g | 5  <-- has neither b nor f (b and f are common to sixes)
# 3 | a cd fg | 5  <-- has only f (b and f are common to sixes)
# 5 | ab d fg | 5  <-- has both b and f (b and f are common to sixes)

# common_in_fives = (a, d, g)

# Sixes
# ---------------
# 0 | abc efg | 6  <-- doesn't have only_in_fives
# 6 | ab defg | 6  <-- has the thing that 2 has after: (2 - common sixes) - (3 - common sixes)
# 9 | abcd fg | 6  <-- contains all of 4

# common_in_sixes = (a, b, f, g)

# only_in_fives = (d)

# only_in_sixes = (b, f)

def alphabetize(str):
	return "".join(sorted(str))

def containsAny(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    return 1 in [c in str for c in set]

def containsAll(str, set):
    """ Check whether sequence str contains ALL of the items in set. """
    return 0 not in [c in str for c in set]

def common(codes):
	commons = Counter()
	for code in codes:
		commons.update(code)
	# print(f'Commons is {commons}')
	temp = Counter(el for el in commons.elements() if commons[el] == len(codes))	
	return list(temp.keys());
	

def decode(displays):

	running_total = 0

	# print(f'Combos are: {combos}')
	# print(f'SSDs are: {ssds}')

	for (combos, ssds) in displays:

		print('-----------------')

		# solution is currently empty
		sol = {}
		fives = []
		sixes = []
		four = ''
		for combo in combos:
			sol[combo] = ''

		for combo in combos:
			if (len(combo) == 2):
				sol[combo] = 1
			elif (len(combo) == 4):
				sol[combo] = 4
				four = combo
			elif (len(combo) == 3):
				sol[combo] = 7
			elif (len(combo) == 7):
				sol[combo] = 8

			elif (len(combo)) == 5:
				fives.append(combo)
			elif (len(combo)) == 6:
				sixes.append(combo)

		common_fives = common(fives)
		common_sixes = common(sixes)
		only_in_fives = [x for x in common_fives if x not in common_sixes]
		only_in_sixes = [x for x in common_sixes if x not in common_fives]
		# print(f'Fives is {fives}')
		# print(f'Common among fives: {common_fives}')
		# print(f'Sixes is {sixes}')
		# print(f'Common among sixes: {common_sixes}')
		# print(f'Only in fives: {only_in_fives}')
		# print(f'Only in sixes: {only_in_sixes}')

		# 2 is in fives but has none of the only_in_sixes
		# 5 is in fives and has both of the only_in_sixes
		# 3 is in fives and has only one of the only_in_sixes

		sixnine = sixes # but right now it still has 0

		for f in fives:
			# any = containsAny(f, set(only_in_sixes))
			# all = containsAll(f, set(only_in_sixes))
			# if all and any:
			# 	sol[f] = 5
			# 	twothree.remove(f) # now twothree is correct
			# if not all and any:
			# 	sol[f] = 3
			# if not all and not any:
			# 	sol[f] = 2
			if only_in_sixes[0] in f and only_in_sixes[1] in f:
				sol[f] = 5
			elif only_in_sixes[0] in f or only_in_sixes[1] in f:
				sol[f] = 3
			else:
				sol[f] = 2

		# 0 is in sixes but has none of the only_in_fives
		for s in sixes:
			if only_in_fives[0] not in s:
 				sol[s] = 0
 				sixnine.remove(s) # now twothree is correct

 		# 9 contains all the characters of 4
		first_is_nine = 1
		for c in list(four):
			print(c)
			if c not in sixnine[0]:
				first_is_nine = 0
		if first_is_nine:
			sol[sixnine[0]] = 9
			sol[sixnine[1]] = 6
		else:
			sol[sixnine[0]] = 6
			sol[sixnine[1]] = 9

		### DAMN THIS CHALLENGE
		alphasol = {}
		for dammit in sol.keys():
			hell = alphabetize(dammit)
			alphasol[hell] = sol[dammit]

		print(f'Solution is: {sol}')
		print(f'Alphasol is: {alphasol}')

		result = ''
		for ssd in ssds:
			result = result + str(alphasol[alphabetize(ssd)])

		print(f'FINALLY! {result}')

		running_total = running_total + int(result)



	return running_total


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

	running_total = decode(displays)

	print(f'Sweet Baby Jesus: {running_total}')

	print(f'Should be 61229 for test file.')

	print("Done!")

main('input.txt')

