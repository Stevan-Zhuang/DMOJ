input = __import__('sys').stdin.readline
MAXN = 100001

n_items, n_queries = [int(data) for data in input().split()]
sum_BITree = [0] * (n_items + 1)
count_BITree = [0] * MAXN

def update(BITree, idx, val, limit):
    while idx <= limit:
        BITree[idx] += val
        idx += idx & -idx

def query(BITree, idx):
    result = 0
    while idx > 0:
        result += BITree[idx]
        idx -= idx & -idx
    return result

arr = [int(data) for data in input().split()]
for idx, item in enumerate(arr):
    update(sum_BITree, idx + 1, item, n_items)
    update(count_BITree, arr[idx], 1, MAXN)

for _ in range(n_queries):
    tokens = input().split()
    op = tokens[0]
    if op == 'C':
        idx, val = int(tokens[1]), int(tokens[2])
        update(sum_BITree, idx, -arr[idx - 1] + val, n_items)
        update(count_BITree, arr[idx - 1], -1, MAXN)
        arr[idx - 1] = val
        update(count_BITree, arr[idx - 1], 1, MAXN)
    if op == 'S':
        left, right = int(tokens[1]), int(tokens[2])
        print(query(sum_BITree, right) - query(sum_BITree, left - 1))
    if op == 'Q':
        val = int(tokens[1])
        print(query(count_BITree, val))
