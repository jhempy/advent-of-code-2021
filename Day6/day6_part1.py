# day6_part1.py

def day(fish):
	new_population = []
	babies = 0
	for f in fish:
		f -= 1
		if f < 0:
			babies += 1
			f = 6
		new_population.append(f)
	new_population += [8] * babies
	return new_population

def calculate_fish_population(fish, days):
	yesterday_total = 0
	for d in range(0, days):
		yesterday_total = len(fish)
		fish = day(fish)
		today_total = len(fish)
		print("Day: ", d, "Fish: ", today_total, "New: ", today_total - yesterday_total)
		print("Fish: ", fish)
	return fish

def parse_input_file(file):
	fish = []
	f = open(file, "r")
	for line in f:
		t = list(map(int, line.split(',')))
		fish = fish + t
	f.close()
	return fish

def main(file):
	print("Starting...")
	days = 0
	fish = parse_input_file(file)
	print("Fish start as: ")
	print(fish)
	days = 18
	fish = calculate_fish_population(fish, days)
	print("Fish end as: ")
	print(fish)
	print("Fish count is now: ")
	print(len(fish))
	print("Done!")

main('test.txt')