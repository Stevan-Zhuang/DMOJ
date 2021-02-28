n_rows = int(input())
n_cols = int(input())
n_strokes = int(input())

row_strokes = [False] * n_rows
col_strokes = [False] * n_cols

for _ in range(n_strokes):
    loc, idx = input().split()
    idx = int(idx) - 1
    if loc == 'R':
        row_strokes[idx] = not row_strokes[idx]
    elif loc == 'C':
        col_strokes[idx] = not col_strokes[idx]

grid = [[False] * n_cols for _ in range(n_rows)]
for row, stroke in enumerate(row_strokes):
    if stroke:
        for col in range(n_cols):
            grid[row][col] = not grid[row][col]
for col, stroke in enumerate(col_strokes):
    if stroke:
        for row in range(n_rows):
            grid[row][col] = not grid[row][col]

print(sum(sum(row) for row in grid))
