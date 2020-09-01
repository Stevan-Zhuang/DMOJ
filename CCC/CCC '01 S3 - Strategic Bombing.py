from collections import defaultdict

network = defaultdict(set)

paths = []
data = input()
while data != "**":
    paths.append(data)
    start_point = data[0]
    end_point = data[1]
    network[start_point].add(end_point)
    network[end_point].add(start_point)
    data = input()

ab_paths = []
def get_paths(path, end):
    if path[-1] == end:
        ab_paths.append(path)
        return
    for point in network[path[-1]]:
        if point not in path:
            get_paths(path + point, end)

get_paths("A", "B")

valid_roads = [path for path in paths
               if all(path in ab_path or path[::-1] in ab_path
                      for ab_path in ab_paths)]

for road in valid_roads:
  print(road)
print("There are {} disconnecting roads.".format(len(valid_roads)))
