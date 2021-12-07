# day7_part1.py

from collections import Counter

def energy_cost(start, end, crabs):
	cost = abs(start - end) * crabs
	return cost

def energy_per_h(h, crabs):
	consumption = 0
	for start in crabs.keys():
		consumption += energy_cost(start, h, crabs[start])
	return consumption

def parse_input_file(file): 
	crabs = []
	f = open(file, "r")
	for line in f:
		t = list(map(int, line.split(',')))
		crabs = crabs + t
	f.close()
	return Counter(crabs)

def main(file):
	print("Starting...")
	crabs = parse_input_file(file)
	print(f"Crabs start as: {crabs}")

	min_h = min(crabs.keys())
	max_h = max(crabs.keys())
	print(f"Min h: {min_h}")
	print(f"Max h: {max_h}")

	energy_costs = Counter()
	for h in range(min_h, max_h):
		energy_costs[h] = energy_per_h(h, crabs)	
	print(energy_costs)

	cheapest = min(energy_costs.values())
	print(f"Cheapest is {cheapest}")

	print("Done!")

main('input.txt')
