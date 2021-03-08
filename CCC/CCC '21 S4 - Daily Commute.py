from collections import deque
input = __import__('sys').stdin.readline
INF = 0x3f3f3f3f

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
    idx += 1
    idx += n_stations
    segment_tree[idx] = value
    while idx > 1:
        segment_tree[idx >> 1] = min(segment_tree[idx], segment_tree[idx ^ 1])
        idx >>= 1

path = [int(data) for data in input().split()]
for idx in range(n_stations):
    update(idx, min_dist[path[idx]] + idx)

for _ in range(n_days):
    x, y = [int(data) - 1 for data in input().split()]
    path[x], path[y] = path[y], path[x]

    update(x, min_dist[path[x]] + x)
    update(y, min_dist[path[y]] + y)

    print(segment_tree[1])
