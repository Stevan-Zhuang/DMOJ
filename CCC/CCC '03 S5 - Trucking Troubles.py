input = __import__('sys').stdin.readline

n_cities, n_roads, n_dests = [int(data) for data in input().split()]
roads = [tuple(int(data) for data in input().split())[::-1]
         for _ in range(n_roads)]
destinations = set(int(input()) for _ in range(n_dests)) | {1}

for weight, city_x, city_y in sorted(roads, reverse=True):
    destinations -= {city_x, city_y}
    if len(destinations) == 0:
        print(weight)
        break
