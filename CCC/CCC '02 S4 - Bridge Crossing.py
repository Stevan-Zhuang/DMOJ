limit = int(input())
n_people = int(input())

data = [(input(), int(input())) for _ in range(n_people)]
names, times = zip(*data)

dp = [0] + [float('inf')] * n_people
dp_names = [[0]] + [[] for _ in range(n_people)]

for idx in range(1, n_people + 1):
    max_time = 0
    for shift in range(1, min(idx, limit) + 1):
        max_time = max(max_time, times[idx - shift])
        if dp[idx] > dp[idx - shift] + max_time:
            dp[idx] = dp[idx - shift] + max_time
            dp_names[idx] = dp_names[idx - shift] + [idx]

print(f"Total Time: {dp[-1]}")
n_groups = len(dp_names[-1]) - 1
for idx in range(n_groups):
    start, end = dp_names[-1][idx], dp_names[-1][idx + 1]
    print(" ".join(names[start: end]))
