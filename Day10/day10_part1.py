# day10_part1.py

def function():
	return 1

def parse_input_file(file):
	lines = []
	f = open(file, "r")
	for l in f:
		lines.append(l.strip())
	f.close()
	return(lines)

def main(file):
	# Setup
	lines = parse_input_file(file)
	
	# Check
	
	# Calculate results
	print("Done!")


main('test.txt')
