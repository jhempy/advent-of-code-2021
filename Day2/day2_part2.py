# day2_part2.py

depth = 0
horizontal = 0
aim = 0

f = open("input.txt", "r")

for command in f:
    parts = command.split(' ', 1)
    verb = parts[0]
    distance = int(parts[1])

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
#     It increases your horizontal position by X units.
#     It increases your depth by your aim multiplied by X.

    if (verb == 'forward'):
        horizontal = horizontal + distance
        depth = depth + (aim * distance)
    if (verb == 'down'):
        aim = aim + distance
    if (verb == 'up'):
        aim = aim - distance

    print(verb, distance, horizontal, depth, horizontal * depth)

f.close()