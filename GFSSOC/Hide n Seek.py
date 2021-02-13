import sys
from itertools import permutations
input = sys.stdin.readline
n_rows, n_cols, n_hiders = [int(data) for data in input().split()]

grid = [input() for _ in range(n_rows)]

hiders = []
idx = 0
for row in range(n_rows):
    for col in range(n_cols):
        if grid[row][col] == 'G':
            start_pos = (row, col)
        if grid[row][col] == 'H':
            hiders.append(((row, col), idx))
            idx += 1

moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
min_hider_dist = [[float('inf')] * (n_hiders + 1) for _ in range(n_hiders + 1)]

for (hider, hider_idx) in hiders + [(start_pos, n_hiders)]:
    min_dist = [[float('inf')] * n_cols for _ in range(n_rows)]
    y, x = hider
    min_dist[y][x] = 0

    queue = [hider]
    while queue:
        row, col = queue.pop(0)
        for (x, y) in moves:
            new_row, new_col = row + y, col + x
            if (    0 <= new_row < n_rows and 0 <= new_col < n_cols
                    and grid[new_row][new_col] != 'X'
                    and min_dist[new_row][new_col] > min_dist[row][col] + 1):
                min_dist[new_row][new_col] = min_dist[row][col] + 1
                queue.append((new_row, new_col))

    for (other_hider, other_hider_idx) in hiders + [(start_pos, n_hiders)]:
        if hider_idx != other_hider_idx:
            y, x = other_hider
            min_hider_dist[hider_idx][other_hider_idx] = min_dist[y][x]

best_path = float('inf')
for path in permutations(range(n_hiders), n_hiders):
    path = [n_hiders] + list(path)
    path_dist = 0
    for idx in range(len(path) - 1):
        start, end = path[idx], path[idx + 1]
        path_dist += min_hider_dist[start][end]
    best_path = min(best_path, path_dist)

print(best_path)

"""
3 5 2
..H..
..X.H
G...X
"""
