# day6_part2.py

from collections import Counter

def day(fish):
	new_fish = Counter()
	babies = 0
	for k in fish.keys():
		v = fish[k]
		if k == 0:
			new_fish[8] += v
			new_fish[6] += v
		else:
			new_fish[k-1] += v
	return(new_fish)


def calculate_fish_population(fish, days):
	for d in range(0, days):
		yesterday_total = sum(fish.values())
		fish = day(fish)
		today_total = sum(fish.values())
		print("Day: ", d, ", Fish: ", today_total, ", New: ", today_total - yesterday_total)
		print("Fish: ", fish)
	return fish


def parse_input_file(file): 
	fish = []
	f = open(file, "r")
	for line in f:
		t = list(map(int, line.split(',')))
		fish = fish + t
	f.close()
	return Counter(fish)

def main(file):
	print("Starting...")
	fish = parse_input_file(file)
	print("Fish start as: ")
	print(fish)
	days = 256
	fish = calculate_fish_population(fish, days)
	print("Fish end as: ")
	print(fish)
	print("Fish count is now: ")
	print(sum(fish.values()))
	print("Done!")

main('input.txt')
