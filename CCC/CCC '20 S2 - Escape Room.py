import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

num_rows = int(input())
num_cols = int(input())

grid = [[int(data) for data in input().split()] for row in range(num_rows)]
visited = [[False] * (num_cols + 1) for row in range(num_rows + 1)]
visited[1][1] = True

network = [[] for _ in range(1000001)]
for row in range(1, num_rows + 1):
    for col in range(1, num_cols + 1):
        network[row * col].append((col, row))

def dfs(col, row):
    if (col, row) == (num_cols, num_rows):
        return True
    for new_col, new_row in network[grid[row - 1][col - 1]]:
        if not visited[new_row][new_col]:
            visited[new_row][new_col] = True
            if dfs(new_col, new_row):
                return True

print("yes" if dfs(1, 1) else "no")
