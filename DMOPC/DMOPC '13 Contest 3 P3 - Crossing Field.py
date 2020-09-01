import sys
sys.setrecursionlimit(1000000)

field_size, max_elevation = [int(data) for data in input().split()]
field = [[int(data) for data in input().split()] for row in range(field_size)]

been_to = [[False for col in range(field_size)] for row in range(field_size)]

orients = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def can_cross(col, row):
    been_to[row][col] = True
    if col == field_size - 1 and row == field_size - 1:
        return True

    for orient in orients:
        if (0 <= col + orient[0] < field_size and 0 <= row + orient[1] < field_size and
                abs(field[row][col] - field[row + orient[1]][col + orient[0]]) <= max_elevation and
                not been_to[row + orient[1]][col + orient[0]]):
            if can_cross(col + orient[0], row + orient[1]):
                return True

print("yes" if can_cross(0, 0) else "no")
