import sys
input = sys.stdin.readline

num_houses, num_pipes, enhance = [int(data) for data in input().split()]

pipes = []
for idx in range(num_pipes):
    house, adj_house, cost = [int(data) for data in input().split()]
    pipes.append((cost, not idx < num_houses - 1, house, adj_house))
pipes.sort()

parent = [*range(num_houses + 1)]
rank = [0] * (num_houses + 1)

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    if rank[x] < rank[y]: 
        parent[x] = y 
    elif rank[x] > rank[y]: 
        parent[y] = x 
    else: 
        parent[y] = x 
        rank[x] += 1

tree_size = 0
days = 0
max_cost = 0
for idx, (cost, new, x, y) in enumerate(pipes):
    if tree_size >= num_houses - 1:
        break
    x_root, y_root = find(x), find(y)
    if x_root != y_root:
        max_cost = cost
        union(x_root, y_root)
        tree_size += 1
        if new:
            days += 1

parent = [*range(num_houses + 1)]
rank = [0] * (num_houses + 1)

_, new, _, _ = pipes[idx - 1]
if new:
    for cost, new, x, y in pipes:
        x_root, y_root = find(x), find(y)
        if x_root != y_root:
            if cost < max_cost or not new and cost == max_cost:
                union(x_root, y_root)
            elif not new and cost <= enhance:
                days -= 1
                break

print(days)
