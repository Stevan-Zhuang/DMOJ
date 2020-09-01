inside_edges = []
edge_to_pen = {}

num_pens = int(input())
for pen_idx in range(num_pens):
    data = [int(data) for data in input().split()]

    num_edges = data[0]
    corners = data[1: num_edges + 1]
    edges = [tuple(sorted([corners[idx], corners[(idx + 1) % num_edges]]))
             for idx in range(num_edges)]
    edge_costs = data[num_edges + 1:]

    for idx in range(num_edges):
        if edges[idx] in edge_to_pen:
            other_pen_idx, _ = edge_to_pen.pop(edges[idx])
            inside_edges.append((edge_costs[idx], pen_idx, other_pen_idx))
        else:
            edge_to_pen[edges[idx]] = (pen_idx, edge_costs[idx])

outside_edges = []
outside_idx = num_pens
for pen_idx, cost in edge_to_pen.values():
    outside_edges.append((cost, pen_idx, outside_idx))

def kruskal(edges, n):
    edges.sort()

    parents = [edge for edge in range(n)]
    def find(x):
        while x != parents[x]:
            x = parents[x]
        return x

    total_cost = 0
    for cost, x, y in edges:
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            total_cost += cost
            parents[x_root] = y_root

    return total_cost

print(min(kruskal(inside_edges, num_pens),
          kruskal(inside_edges + outside_edges, num_pens + 1)))
