# day21_part1.py

import itertools
from collections import Counter

ongoing = []
wins = {}
wins[1] = []
wins[2] = []
player = 1

def count_universes(games):
    ucount = 0
    for g in games:
        ucount = ucount + g.universes
    return ucount

def dedupe(games):
    print(f'Deduping new games...')
    uniques = []
    # print(f'  Started with {len(games)} new games ({count_universes(games)} universes)')
    for g in games:
        found = False
        for u in uniques:
            if g == u:
                u.universes = u.universes + g.universes
                found = True
        if not found:
            uniques.append(g)
    # print(f'  Ended with {len(uniques)} new games ({count_universes(uniques)} universes)')
    return uniques

def generate_combos():
    # Dirac quantum die
    c = []
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                c.append(i + j + k)
    return Counter(c)

class game:

    id_iter = itertools.count()

    def __init__(self, x1, x2, u):
        self.id = next(game.id_iter)
        self.universes = u
        self.player = 1
        self.start = {}
        self.start[1] = x1
        self.start[2] = x2
        self.current = {}
        self.current[1] = x1
        self.current[2] = x2
        self.total = {}
        self.total[1] = 0
        self.total[2] = 0

    def __eq__(self, other):
        return self.id != other.id and self.current[1] == other.current[1] and self.current[2] == other.current[2] and self.total[1] == other.total[1] and self.total[2] == other.total[2]

    def __str__(self):
        return f'Game {self.id}: {self.universes} universes'

    def copy(self, u):
        n = game(self.start[1], self.start[2], 1)
        n.universes = self.universes * u
        n.current[1] = self.current[1]
        n.current[2] = self.current[2]
        n.total[1] = self.total[1]
        n.total[2] = self.total[2]
        return n

def next_player():
    global player
    if player == 1:
        player = 2
    else:
        player = 1

def main():
    
    global ongoing, wins, player

    ongoing.append(game(5, 9, 1))
    loops = 0

    while ongoing:

        loops = loops + 1
        print(f'Starting a new outer loop ({loops}): {len(ongoing)} games, {count_universes(ongoing)} universes')
        wins1 = count_universes(wins[1])
        wins2 = count_universes(wins[2]) 
        print(f'  Player is {player}')
        print(f'  Games already won by player 1: {wins1}')
        print(f'  Games already won by player 2: {wins2}')

        temp = []
        games_in_this_loop = 0

        for g in ongoing:

            combos = generate_combos()
            for c in combos.items():

                n = g.copy(c[1])

                games_in_this_loop = games_in_this_loop + n.universes

                # Calculate current space
                n.current[player] = (n.current[player] + c[0]) % 10
                if n.current[player] == 0:
                    n.current[player] = 10;
                
                # Increase player's total
                n.total[player] = n.total[player] + n.current[player]

                if n.total[player] > 20:
                    wins[player].append(n)
                else:
                    temp.append(n)

        wins1 = count_universes(wins[1])
        wins2 = count_universes(wins[2])
        print(f'  New universes considered: {games_in_this_loop}')
        print(f'  Games now won by player 1: {wins1}')
        print(f'  Games now won by player 2: {wins2}')

        ongoing = dedupe(temp)

        next_player()

    print(f'')
    print(f'Ongoing games: {len(ongoing)}')
    wins1 = count_universes(wins[1])
    wins2 = count_universes(wins[2])
    print(f'Games won by player 1: {len(wins[1])}, {wins1} (should be 444356092776315)')
    print(f'Games won by player 2: {len(wins[2])}, {wins2} (should be 341960390180808)')

    print(f'Done!')

main()

