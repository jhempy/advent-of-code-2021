# day21_part1.py


face = 0
roll_counter = 0
player = 1

def next_player():
    global player
    if player == 1:
        player = 2
    else:
        player = 1

def roll():
    global face, roll_counter
    roll_counter = roll_counter + 1
    if face == 100:
        face = 1
    else:
        face = face + 1
    return face

def main():
    global roll_counter, player

    start = {}
    start[1] = 5
    start[2] = 9
    current = {}
    current[1] = 5
    current[2] = 9
    total = {}
    total[1] = 0
    total[2] = 0

    while total[1] < 1000 and total[2] < 1000:
        print(f'Player is {player}')
        spaces = 0
        for i in range(3):
            x = roll()
            print(f'  Roll is {x}')
            spaces = spaces + x
        print(f'  Spaces is {spaces}')
        current[player] = (current[player] + spaces) % 10
        if current[player] == 0:
            current[player] = 10;
        print(f'  Current is {current[player]}')
        total[player] = total[player] + current[player]
        print(f'  Total is {total[player]}')
        next_player()

    print(f'Player 1 total: {total[1]}')
    print(f'Player 2 total: {total[2]}')
    print(f'Number of rolls: {roll_counter}')
    magic = min(total[1], total[2]) * roll_counter
    print(f'Magic number: {magic}')
    print(f'Done!')

main()

