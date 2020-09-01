n_cities, n_roads, n_dests = [int(data) for data in input().split()]

bridges = []
for road in range(n_roads):
    city_x, city_y, max_weight = [int(data) for data in input().split()]
    bridges.append((max_weight, city_x, city_y))

cities = [integer + 1 for integer in range(n_cities)]
destinations = [int(input()) for _ in range(n_dests)]

def kruskal_prim():
    values = [0] * (n_cities + 1)
    visited = [False] * (n_cities + 1)

    for cost, city_x, city_y in sorted(bridges, reverse=True):
        if not (visited[city_x] and visited[city_y]):

            values[city_x] = max(cost, values[city_x])
            values[city_y] = max(cost, values[city_y])

            visited[city_x] = True
            visited[city_y] = True

    return min(values[dest] for dest in destinations)

print(kruskal_prim())
