from math import inf

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
results = []
for case in range(int(input())):
    grid_size = int(input())
    grid = [[int(input()) for col in range(grid_size)]
            for row in range(grid_size)]
    min_oxygen = [[inf for col in range(grid_size)]
                  for row in range(grid_size)]
    start_elevation = grid[0][0]

    queue = [(0, 0, 0)]
    while queue:
        col, row, oxygen = queue.pop(0)
        if oxygen >= min_oxygen[row][col]:
            continue
        min_oxygen[row][col] = oxygen
        if (col, row) == (grid_size, grid_size):
            continue

        for dir in directions:
            new_col, new_row = col + dir[0], row + dir[1]
            if (    0 <= new_col < grid_size and 0 <= new_row < grid_size and
                    abs(grid[row][col] - grid[new_row][new_col]) <= 2):
                new_oxygen = (oxygen + 1
                              if grid[row][col] > start_elevation or
                              grid[new_row][new_col] > start_elevation
                              else oxygen)
                queue.append((new_col, new_row, new_oxygen))

    results.append(str(min_oxygen[-1][-1]) if min_oxygen[-1][-1] < inf else "CANNOT MAKE THE TRIP")

print("\n\n".join(results))
