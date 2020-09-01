num_rows, num_cols = [int(data) for data in input().split()]
num_paths = [[0] * num_cols for row in range(num_rows)]
num_paths[0][0] = 1

num_cats = int(input())
for cat in range(num_cats):
    row, col = input().split()
    row, col = int(row) - 1, int(col) - 1
    num_paths[row][col] = -1

for row in range(num_rows):
    for col in range(num_cols):
        if num_paths[row][col] != -1:
            left = num_paths[row][col - 1] if num_paths[row][col - 1] != -1 else 0
            up = num_paths[row - 1][col] if num_paths[row - 1][col] != -1 else 0
            cur = num_paths[row][col]
            num_paths[row][col] = max(left + up, cur)

print(num_paths[-1][-1])
