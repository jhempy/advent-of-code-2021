# day9_part1.py

from collections import Counter

def find_lowest_neighbor(depths, neighbors):
	t = {}
	for n in neighbors:
		d = depths[n[0]][n[1]]
		t[d] = n
	# print(f'Lowest neighbor is: {t}')
	return t[sorted(t)[0]]

def find_neighbors(depths, r, c):
	neighbors = []
	clen = len(depths[0])
	rlen = len(depths)
	if c > 0:
		# add neighbor to the west
		neighbors.append([r, c-1])
	if c < clen-1:
		# add neighbor to the east
		neighbors.append([r, c+1])
	if r > 0:
		# add neighbor to the north
		neighbors.append([r-1, c])
	if r < rlen-1:
		# add neighbor to the south
		neighbors.append([r+1, c])
	# print(neighbors)
	return neighbors

def basin(feeds_tos, m, n):
	feeders = [[m, n]]
	matches = []
	# print(f'Calculating feeders for [{m},{n}]')
	for (i, r) in enumerate(feeds_tos):
		for (j, c) in enumerate(feeds_tos[i]):
			# print(f'  {i},{j}: Comparing {feeds_tos[i][j]} to [{m}, {n}]')
			if feeds_tos[i][j] == [m, n]:
				# print('  Match!')
				matches.append([i, j])
	# print(f'  Matches: {matches}')
	for x in matches:
		feeders = feeders + basin(feeds_tos, x[0], x[1])
	return feeders

def find_feeds_tos(depths):
	f2 = []
	for (i, r) in enumerate(depths):
		r = []
		for (j, c) in enumerate(depths[i]):
			if depths[i][j] == 0:
				# lowest points never feed anywhere.
				r.append([])
			elif depths[i][j] == 9:
				# highest points don't feed anywhere, either (per instructions)
				r.append([])
			else:
				neighbors = find_neighbors(depths, i, j)
				lowest = find_lowest_neighbor(depths, neighbors)
				if depths[lowest[0]][lowest[1]] < depths[i][j]:
					r.append(lowest)
				else:
					r.append([])
		f2.append(r)
	return f2

def find_basin_centers(lows):
	b = []
	for (i, r) in enumerate(lows):
		for (j, c) in enumerate(lows[i]):
			if lows[i][j] == 1:
				b.append([i,j])
	return b

def risk(d):
	return d + 1

def calculate_risk(depths, lows):
	t = 0
	for (i, r) in enumerate(lows):
		for (j, c) in enumerate(lows[i]):
			if lows[i][j] == 1:
				t = t + risk(depths[i][j])
	return t

def low(depths, r, c):
	# print(f'Calculating lowness of ({r},{c}) = {depths[r][c]}')
	is_clow = calc_clow(depths, r, c)
	# print(f'  is_clow is {is_clow}')
	is_rlow = calc_rlow(depths, r, c)
	# print(f'  is_rlow is {is_rlow}')
	is_low = is_clow * is_rlow
	# print(f'  is_low is {is_low}')
	return is_low

def calc_clow(depths, r, c):
	# print(f'  Calculating column lowness of ({r},{c})')
	# is this point lower than the one to the left (if exists) 
	# and the one to the right (if exists)?
	is_low = []
	clen = len(depths[0])
	# print(f'    clen is {clen}')
	if c > 0:
		# print(f'      c > 0 (to the left)')
		is_low.append(depths[r][c-1] > depths[r][c])
	if c < clen-1:
		# print(f'      c < clen-1 (to the right)')
		is_low.append(depths[r][c+1] > depths[r][c])
	if len(is_low) == 1:
		return is_low[0]
	else:
		return is_low[0] and is_low[1]

def calc_rlow(depths, r, c):
	# print(f'  Calculating row lowness of ({r},{c})')
	# is this point lower than the one above (if exists) 
	# and the one below (if exists)?
	is_low = []
	rlen = len(depths)
	# print(f'    rlen is {rlen}')
	if r > 0:
		# print(f'      r > 0 (above)')
		is_low.append(depths[r-1][c] > depths[r][c])
	if r < rlen-1:
		# print(f'      r < rlen-1 (below)')
		is_low.append(depths[r+1][c] > depths[r][c])
	if len(is_low) == 1:
		return is_low[0]
	else:
		return is_low[0] and is_low[1]
	
def calculate_lows(depths):
	lows = []
	for (i, r) in enumerate(depths):
		t = []
		for (j, c) in enumerate(r):
			t.append(low(depths, i, j))
		lows.append(t)
	return lows;

def parse_input_file(file): 
	depths = []
	f = open(file, "r")
	for line in f:
		depths.append(list(map(int, list(line.rstrip('\n')))))
	f.close()
	return depths

def main(file):
	print("Starting...")
	depths = parse_input_file(file)
	# print(f'Input data:')
	for r in range(len(depths)):
		print(depths[r])

	lows = calculate_lows(depths)
	# for r in range(len(lows)):
	# 	print(lows[r])

	risk = calculate_risk(depths, lows)
	# print(f'Risk is {risk}')

	basin_centers = find_basin_centers(lows)
	print(f'Basin centers are {basin_centers}')

	feeds_tos = find_feeds_tos(depths)
	# print(f'Where every point feeds to:')
	# for r in range(len(feeds_tos)):
	# 	print(feeds_tos[r])

	basin_sizes = []
	for c in basin_centers:
		s = basin(feeds_tos, c[0], c[1])
		basin_sizes.append([c, s])
	# print(f'Basin sizes: {basin_sizes}')

	c = Counter()
	for bs in basin_sizes:
		print(f'Basin: {bs[0]}, Size: {len(bs[1])}')	
		c.update([len(bs[1])])

	# print(c.most_common())
	print(sorted(c.items(), key=lambda i: i))

	print("Done!")

main('input.txt')
