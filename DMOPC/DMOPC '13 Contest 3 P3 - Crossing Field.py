import sys
from collections import deque
input = sys.stdin.readline

N, H = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

visited = [[False for _ in range(N)] for _ in range(N)]
visited[0][0] = True
orients = [(0, 1), (1, 0), (0, -1), (-1, 0)]

queue = deque([(0, 0)])
while queue:
    col, row = queue.pop()
    if col == row == N - 1:
        print("yes")
        sys.exit()

    for orient in orients:
        new_col, new_row = col + orient[0], row + orient[1]
        if (0 <= new_col < N and 0 <= new_row < N and
                abs(field[row][col] - field[new_row][new_col]) <= H and
                not visited[new_row][new_col]):
            visited[new_row][new_col] = True
            queue.append((new_col, new_row))

print("no")
