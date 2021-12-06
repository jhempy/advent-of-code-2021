# day5_part2.py

from collections import Counter

def generate_point_list(x1, y1, x2, y2):
	point_list = []
	# per instructions, only consider horizontal or vertical lines
	if (x1 == x2 or y1 == y2):
		for x in range(x1, x2 + 1 if x2 >= x1 else x2 - 1, 1 if x2 >= x1 else -1): # sneaky!
			for y in range(y1, y2 + 1 if y2 >= y1 else y2 - 1, 1 if y2 >= y1 else -1): #sneaky!
				# print ("x: ", x, ", y: ", y)
				point_list.append((x, y))
	# now, with diagonals!
	elif (abs(x1 - x2) == abs(y1 - y2)):
		for i, x in enumerate(range(x1, x2 + 1 if x2 >= x1 else x2 - 1, 1 if x2 >= x1 else -1)): # sneaky!
			ymod = +i if y2 >= y1 else -i
			y = y1 + ymod
			# print ("x: ", x, ", y: ", y)
			point_list.append((x, y))
	return point_list

def parse_line(line):
	# input format: 'x1, y1 -> x2, y2'
	start, end = line.split('->')
	x1, y1 = start.split(',')
	x2, y2 = end.split(',')
	return(x1, y1, x2, y2)

def parse_input_file(file):
	lines = []
	f = open(file, "r")
	for line in f:
		t = list(map(int, parse_line(line.strip())))
		lines.append(t)
	f.close()
	return lines

def main(file):
	print("Starting main...")

	lines = parse_input_file(file)
	print("Lines: ")
	print(lines)

	points = []
	for line in lines:
		for p in generate_point_list(line[0], line[1], line[2], line[3]):
			points.append(p)	
	print("Points: ")
	print(points)

	counts = Counter(points)
	print("Counts: ")
	print(counts)

	threshold = 2
	intersections = Counter(dict(filter(lambda x: x[1] >= threshold, counts.items())))
	print("Intersections > ", threshold)
	print(len(intersections))

	print("Done")

main('input.txt')