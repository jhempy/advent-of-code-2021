# day2_part1.py

f = open("input.txt", "r")
depth = 0
horizontal = 0
message = '--'
for command in f:
    parts = command.split(' ', 1)
    verb = parts[0]
    distance = int(parts[1])

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

    if (verb == 'forward'):
        horizontal = horizontal + distance
    if (verb == 'down'):
        depth = depth + distance
    if (verb == 'up'):
        depth = depth - distance

    print(verb, distance, horizontal, depth, horizontal * depth)

f.close()