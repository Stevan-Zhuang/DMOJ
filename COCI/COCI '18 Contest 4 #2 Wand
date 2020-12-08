input = __import__("sys").stdin.readline

num_wiz, num_duels = [int(data) for data in input().split()]

graph = [[] for _ in range(num_wiz + 1)]
for _ in range(num_duels):
    adj_vertex, vertex = [int(data) for data in input().split()]
    graph[vertex].append(adj_vertex)

visited = set()
endpoint = [0] * (num_wiz + 1)
if len(graph[1]) == 0:
    endpoint[1] = 1

queue = [1]
while queue:
    vertex = queue.pop(0)
    for adj_vertex in graph[vertex]:
        edge = (vertex, adj_vertex)
        if not edge in visited:
            queue.append(adj_vertex)
            visited.add(edge)
            endpoint[adj_vertex] = 1

print("".join(str(data) for data in endpoint[1:]))
