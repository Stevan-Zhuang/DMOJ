from collections import deque

start_col, start_row = [int(data) for data in input().split()]
end_col, end_row = [int(data) for data in input().split()]

possible_moves = [(1, 2), (2, 1), (2, -1), (1, -2),
                  (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

visited = [[False] * (8 + 1) for _ in range(8 + 1)]
queue = deque([(start_row, start_col, 0)])
while queue:
    row, col, steps = queue.popleft()
    if (row, col) == (end_row, end_col):
        print(steps)
        break
    for move in possible_moves:
        new_row, new_col = row + move[0], col + move[1]
        if 1 <= new_row <= 8 and 1 <= new_col <= 8 and not visited[new_row][new_col]:
            queue.append((new_row, new_col, steps + 1))
