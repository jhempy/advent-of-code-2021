# day21_part1.py

import itertools
from collections import Counter

ongoing = []
wins = {}
wins[1] = []
wins[2] = []

def dedupe(games):
    uniques = []
    for g in games:
        if g in uniques:
            for u in uniques:
                if g == u:
                    u.universes = u.universes + g.universes
                    # print(f'Adding {g.id} to {u.id}')
                    # print(g)
                    # print(u)
        else:
            uniques.append(g)
    return uniques

def generate_combos():
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
        self.roll_counter = 0
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
        return self.id != other.id and self.roll_counter == other.roll_counter and self.player == other.player and self.current[1] == other.current[1] and self.current[2] == other.current[2] and self.total[1] == other.total[1] and self.total[2] == self.total[2]

    def __str__(self):
        return f'Game {self.id}: {self.universes} universes'

    def next_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def copy(self, u):
        n = game(self.start[1], self.start[2], 0)
        n.universes = self.universes + u
        n.roll_counter = self.roll_counter
        n.player = self.player
        n.current[1] = self.current[1]
        n.current[2] = self.current[2]
        n.total[1] = self.total[1]
        n.total[2] = self.total[2]
        return n

def main():
    
    global ongoing, wins

    ongoing.append(game(4, 8, 0))
    
    while ongoing:

        print(f'Starting a new outer loop: {len(ongoing)} ongoing games')
        temp = []

        for g in ongoing:

            print(f'Starting game: {g}')
            combos = generate_combos()
            # print(combos)
            for c in combos.items():

                n = g.copy(c[1])
                # print(f'  Created game ID {n.id} with {n.universes} universes')

                # print(f'    Spaces is {c[0]}')
                n.current[n.player] = (n.current[n.player] + c[0]) % 10
                if n.current[n.player] == 0:
                    n.current[n.player] = 10;
                # print(f'    Current is {n.current[n.player]}')
                n.total[n.player] = n.total[n.player] + n.current[n.player]
                # print(f'    Total is {n.total[n.player]}')

                if n.total[n.player] > 20:
                    wins[n.player].append(n)
                else:
                    n.next_player()
                    temp.append(n)

        ongoing = dedupe(temp)

    print(f'Ongoing games: {len(ongoing)}')
    wins1 = 0
    for w in wins[1]:
        wins1 = wins1 + w.universes
    wins2 = 0
    for w in wins[2]:
        wins2 = wins2 + w.universes
    print(f'Games won by player 1: {wins1} should be 444356092776315')
    print(f'Games won by player 2: {wins2} should be 341960390180808')

    print(f'Done!')

main()

