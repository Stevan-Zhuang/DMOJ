input = __import__('sys').stdin.readline

num_cities, num_queries = [int(data) for data in input().split()]

parent = list(range(num_cities + 1))
rank = [0] * (num_cities + 1)

def union(x, y):
    if rank[x] < rank[y]: 
        parent[x] = y 
    elif rank[x] > rank[y]: 
        parent[y] = x 
    else: 
        parent[y] = x 
        rank[x] += 1

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

for _ in range(num_queries):
    query, x, y = input().split()
    x_root = find(int(x))
    y_root = find(int(y))
    if query == "A":
        if x_root != y_root:
            union(x_root, y_root)
    if query == "Q":
        print("Y" if x_root == y_root else "N")
