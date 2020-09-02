num_rows, num_cols = [int(data) for data in input().split()]
grid = [input() for _ in range(num_rows)]
num_paths = [[0] * (num_cols + 1) for row in range(num_rows + 1)]
num_paths[1][1] = 1

MOD = 1000000007
for row in range(1, num_rows + 1):
    for col in range(1, num_cols + 1):
        if grid[row - 1][col - 1] != '#':
            left = num_paths[row][col - 1]
            up = num_paths[row - 1][col]
            cur = num_paths[row][col]
            num_paths[row][col] = max(left + up, cur) % MOD

print(num_paths[-1][-1])
