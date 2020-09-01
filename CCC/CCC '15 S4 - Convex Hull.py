from heapq import heappop
from heapq import heappush

hull, n_islands, n_routes = [int(data) for data in input().split()]

network = [[] for _ in range(n_islands + 1)]
for _ in range(n_routes):
    island_a, island_b, time, cost = [int(data) for data in input().split()]
    network[island_a].append((time, cost, island_b))
    network[island_b].append((time, cost, island_a))

start_island, end_island = [int(data) for data in input().split()]

max_hulls = [0] * (n_islands + 1)

result = -1
queue = [(0, hull, start_island)]
while queue:
    cur_time, cur_hull, cur_island = heappop(queue)
    max_hulls[cur_island] = cur_hull
    if cur_island == end_island:
        result = cur_time
        break
    
    for time, cost, island in network[cur_island]:
        if cur_hull - cost > max_hulls[island]:
            heappush(queue, (cur_time + time, cur_hull - cost, island))

print(result)
