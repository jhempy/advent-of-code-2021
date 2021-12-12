# day11_part1.py

from collections import Counter

octos = []

def process_flashes():
	flashers = []
	for r in range(len(octos)):
		for c in range(len(octos[0])):
			if octos[r][c] > 9:
				flashers.append([r, c])
				octos[r][c] = 0 # reset this one
	for f in flashers:
		increase_neighbors(f[0], f[1])
	return len(flashers)
	
def increase_all_octos():
	for r in range(len(octos)):
		for c in range(len(octos[0])):
			octos[r][c] = octos[r][c] + 1
	return

def step(s):
	total = 0
	increase_all_octos()
	flashes = process_flashes()
	while flashes > 0:
		total = total + flashes
		flashes = process_flashes()
	print(f'After step {s}:')
	print_octos()
	print(f'--------(mine)------------')
	return total

def increase_neighbors(r, c):
	temp = []
	neighbors = []

	temp.append([r-1, c-1]) 	# add neighbor to the nw
	temp.append([r-1, c]) 	 	# add neighbor to the north
	temp.append([r-1, c+1]) 	# add neighbor to the ne
	temp.append([r, c+1]) 	 	# add neighbor to the east
	temp.append([r, c-1]) 	 	# add neighbor to the west
	temp.append([r+1, c+1]) 	# add neighbor to the se
	temp.append([r+1, c]) 	 	# add neighbor to the south
	temp.append([r+1, c-1]) 	# add neighbor to the sw
	for (tr, tc) in temp:
		try:
			if tr in range(10) and tc in range(10) and octos[tr][tc] > 0: # only increase neighbors who haven't yet flashed
				octos[tr][tc] = octos[tr][tc] + 1
		except IndexError:
			pass
	return

def parse_input_file(file): 
	f = open(file, "r")
	for line in f:
		octos.append(list(map(int, list(line.rstrip('\n')))))
	f.close()
	return

def print_octos():
	for o in range(len(octos)):
		print(''.join(map(str,octos[o])))
	return

def main(file):

	# Import input data
	octos = parse_input_file(file)
	print(f'Input data:')
	print_octos()
	print(f'--------------------')


	# Calculate steps
	total = 0
	for x in range(1,101,1):
		total = total + step(x)

	# Cleanup
	print(f'Total flashes: {total}')
	print("Done!")

main('input.txt')
