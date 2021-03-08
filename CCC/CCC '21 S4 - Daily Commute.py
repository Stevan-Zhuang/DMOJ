from collections import deque
input = __import__('sys').stdin.readline
INF = float('inf')

n_stations, n_paths, n_days = [int(data) for data in input().split()]

network = [[] for _ in range(n_stations + 1)]
for _ in range(n_paths):
    a, b = [int(data) for data in input().split()]
    network[b].append(a)

min_dist = [INF] * (n_stations + 1)
min_dist[n_stations] = 0

queue = deque([(0, n_stations)])
while queue:
    steps, node = queue.popleft()
    for adj_node in network[node]:
        if min_dist[adj_node] > steps + 1:
            min_dist[adj_node] = steps + 1
            queue.append((steps + 1, adj_node))

segment_tree = [INF] * (2 * (n_stations + 1))

def update(idx, value):
    idx += n_stations
    segment_tree[idx] = value
    while idx > 1:
        segment_tree[idx >> 1] = min(segment_tree[idx], segment_tree[idx ^ 1])
        idx >>= 1

def query(left, right):
    result = INF
    left += n_stations
    right += n_stations
    while left < right:
        if left & 1:
            result = min(result, segment_tree[left])
            left += 1
        if right & 1:
            right -= 1
            result = min(result, segment_tree[right])
        left >>= 1
        right >>= 1
    return result

path = [0] + [int(data) for data in input().split()]
for idx in range(1, n_stations + 1):
    steps = idx - 1
    update(idx, min_dist[path[idx]] + steps)

for _ in range(n_days):
    x, y = [int(data) for data in input().split()]
    x_steps, y_steps = x - 1, y - 1

    path[x], path[y] = path[y], path[x]

    update(x, min_dist[path[x]] + x_steps)
    update(y, min_dist[path[y]] + y_steps)

    print(query(1, n_stations + 1))
