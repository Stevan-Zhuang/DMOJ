input = __import__('sys').stdin.readline
num_vertices, num_edges = [int(data) for data in input().split()]

edges = []
adj = [[] for _ in range(num_vertices + 1)]
for _ in range(num_edges):
    x, y = [int(data) for data in input().split()]
    adj[x].append(y)
    edges.append((x, y))

def dfsearch(vertex):
    if vertex == num_vertices:
        return True
    for adj_vertex in adj[vertex]:
        if (vertex, adj_vertex) == edge:
            continue
        if not visited[adj_vertex]:
            visited[adj_vertex] = True
            if dfsearch(adj_vertex):
                return True
  return False

for edge in edges:
    visited = [False] * (num_vertices + 1)
    print("YES" if dfsearch(1) else "NO")
