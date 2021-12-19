# day17_part1.py

from collections import Counter

xmin = None
xmax = None
ymin = None
ymax = None
x_range = []
y_range = []

def parse_input_file(file): 
    global xmin, xmax, ymin, ymax, x_range, y_range
    f = open(file, "r")
    for line in f:
        l = line.rstrip('\n')[12:]
        xs, ys = l.split(', ')
        xs = xs[3:]
        xmin = min(list(map(int, xs.split('..'))))
        xmax = max(list(map(int, xs.split('..'))))
        ys = ys[2:]
        ymin = min(list(map(int, ys.split('..'))))
        ymax = max(list(map(int, ys.split('..'))))
        x_range = range(xmin, xmax + 1, 1)
        y_range = range(ymin, ymax + 1, 1)
    f.close()
    return

class launch:

    def __init__(self, xv, yv):
        self.orig_xvel = int(xv)
        self.xvel = self.orig_xvel
        self.orig_yvel = int(yv)
        self.yvel = self.orig_yvel
        self.startpos = [0, 0]
        self.just_falling = False
        self.path = []
        self.max_height = 0
        self.path.append(self.startpos)
        self.hit_target = False
        self.compute_trajectory()

    def __str__(self):
        out =       f'----------------' + '\n'
        out = out + f'Launch Object:' + '\n'
        out = out + f'  Original velocity: {self.orig_xvel}, {self.orig_yvel}' + '\n'
        out = out + f'  Final velocity:    {self.xvel}, {self.yvel}' + '\n'
        out = out + f'  Path: {self.path}' + '\n'
        out = out + f'  Hit target? {self.hit_target}' + '\n'
        out = out + f'  Max height: {self.max_height}' + '\n'
        out = out + f'----------------' + '\n'
        return out

    def compute_trajectory(self):

        global x_range, y_range

        past_target = False
        in_target = False
        out_of_range = False
        while not past_target and not in_target:

            self.next_location()
            [curx, cury] = self.path[-1]

            # Update max_height?
            if cury > self.max_height:
                self.max_height = cury

            # Is the current position in the target?
            if curx in x_range and cury in y_range:
                in_target = True

            # Is the current position out of range?
            if curx > xmax or cury < ymin:
                # print(f'Point {curx},{cury} is out of range')
                past_target = True

        if past_target:
            return False
        if in_target:
            self.hit_target = True
            return True

    def next_location(self):
        [curx, cury] = self.path[-1]
        nextx = curx + self.xvel
        nexty = cury + self.yvel
        if self.xvel > 0:
            self.xvel = self.xvel - 1
        else: 
            self.just_falling = True
        self.yvel = self.yvel - 1
        self.path.append([nextx, nexty])
        return

def calculate_lowest_x():
    global xmin
    i = 0
    t = i
    while t < xmin:
        i = i + 1
        t = t + i
    return i 

def calculate_highest_y():
    global ymin, ymax
    i = ymax
    t = i
    while t > ymin:
        i = i + 1
        t = t - i
        print(f'i is {i}, t is {t}')
    return i - ymax - 1


def main(file):

    global xmin, xmax, ymin, ymax, x_range, y_range

    parse_input_file(file)
    print(f'Xmin    = {xmin}')
    print(f'Xmax    = {xmax}')
    print(f'Ymin    = {ymin}')
    print(f'Ymax    = {ymax}')
    print(f'X_range = {x_range}')
    print(f'Y_range = {y_range}')
    print('')
    print('')

    heights = []

    # attempts = [[5,3], [6,3], [7,3]]
    # attempts = [[6,-1], [6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [6,6], [6,7], [6,8], [6,9], [6,10], [6,11], [6,12], [6,13], [6,14], [6,15]]

    # for a in attempts:
    #     attempt = launch(a[0], a[1])
    #     print(attempt)
    #     if attempt.hit_target:
    #         heights.append(attempt.max_height)


    lowest_x = calculate_lowest_x()
    highest_y = calculate_highest_y()

    print(f'')
    print(f'Lowest x is {lowest_x}')
    print(f'Highest y is {highest_y}')
    print(f'')

    for x in range (lowest_x - 500, lowest_x + 500):
        for y in range(highest_y - 500, highest_y + 500):
            print(f'Attempting {x}, {y}')
            attempt = launch(x, y)
            # print(attempt)
            if attempt.hit_target:
                heights.append(attempt.max_height)

    c = Counter(heights)
    print(f'Heights achieved: {c}')
    print(f'Total combos that succeed: {len(heights)}')

    # Cleanup
    print('')
    print('Done!')


# main('test.txt')
main('input.txt')
