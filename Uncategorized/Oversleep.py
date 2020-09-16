from collections import deque
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

num_rows, num_cols = [int(data) for data in input().split()]
grid = [input() for _ in range(num_rows)]

visited = [[False] * num_cols for _ in range(num_rows)]

for row in range(num_rows):
  for col in range(num_cols):
    if grid[row][col] == 's':
      start = (col, row, -1)

min_time = -1

queue = deque([start])
while queue:
  col, row, cur_time = queue.popleft()
  if grid[row][col] == 'e':
    min_time = cur_time
    break
  if grid[row][col] == 'X':
    continue
  for hor, ver in directions:
    if (0 <= row + ver < num_rows and 0 <= col + hor < num_cols
        and not visited[row + ver][col + hor]):
      visited[row + ver][col + hor] = True
      queue.append((col + hor, row + ver, cur_time + 1))

print(min_time)
