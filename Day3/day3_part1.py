# day3_part1.py

def calculate_gamma_rate(f):

    # f = open("input.txt", "r")

    # for command in f:
    #     parts = command.split(' ', 1)
    #     verb = parts[0]
    #     distance = int(parts[1])

    #     if (verb == 'forward'):
    #         horizontal = horizontal + distance
    #         depth = depth + (aim * distance)
    #     if (verb == 'down'):
    #         aim = aim + distance
    #     if (verb == 'up'):
    #         aim = aim - distance

    #     print(verb, distance, horizontal, depth, horizontal * depth)

    # f.close()

    return 2;

def calculate_epsilon_rate(f):
    return 1;


def calculate_power_consumption(f):
    gamma_rate = calculate_gamma_rate(f)
    epsilon_rate = calculate_epsilon_rate(f)
    return gamma_rate * epsilon_rate

def main(f):
    power_consumption = calculate_power_consumption(f)
    print(power_consumption)

main('test.txt')
