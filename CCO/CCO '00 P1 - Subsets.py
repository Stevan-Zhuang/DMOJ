from collections import defaultdict
from collections import deque

sets = defaultdict(set)
adj = defaultdict(list)
N = int(input())
for _ in range(N):
    X, _, S = input().split()
    sets[X]
    if S.isupper():
        sets[S]
        adj[S].append(X)
    if S.islower():
        sets[X].add(S)

for root_node in sets:
    if len(sets[root_node]) > 0:
        visited = defaultdict(bool)
        visited[root_node] = True
        queue = deque([root_node])
        while queue:
            node = queue.popleft()
            for adj_node in adj[node]:
                if not visited[adj_node]:
                    sets[adj_node].update(sets[root_node])
                    visited[adj_node] = True
                    queue.append(adj_node)

for name in sorted(sets):
    str_set = "{" + ",".join(sorted(sets[name])) + "}"
    print(f"{name} = {str_set}")
