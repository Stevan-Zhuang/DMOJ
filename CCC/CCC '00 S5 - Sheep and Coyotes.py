from decimal import Decimal
from collections import namedtuple
input = __import__('sys').stdin.readline
Point = namedtuple('Point', ['x', 'y'])

num_sheeps = int(input())
sheeps = [Point(Decimal(input()), Decimal(input()))
          for idx in range(num_sheeps)]
valid = [True] * num_sheeps

for idx1 in range(num_sheeps):
    valid_left, valid_right = 0, 1000
    for idx2 in range(num_sheeps):
        if idx1 == idx2:
            continue
        sheep1, sheep2 = sheeps[idx1], sheeps[idx2]
        if valid[idx1] and valid[idx2]:
            middle = Point((sheep1.x + sheep2.x) / 2, (sheep1.y + sheep2.y) / 2)
            rise, run = (sheep2.y - sheep1.y), (sheep2.x - sheep1.x)
            if run == 0:
                if rise < 0: valid[idx1] = False
                if rise > 0: valid[idx2] = False
                continue
            elif rise == 0:
                x_inter = middle.x
            else:
                slope = rise / run
                perp_slope =  -1 / slope
                x_inter = -middle.y / perp_slope + middle.x

            if run < 0: valid_left = max(x_inter, valid_left)
            if run > 0: valid_right = min(x_inter, valid_right)

    if valid_left > valid_right:
        valid[idx1] = False

for idx in range(num_sheeps):
    if valid[idx]:
        print(f"The sheep at ({sheeps[idx].x:.2f}, {sheeps[idx].y:.2f}) might be eaten.")
