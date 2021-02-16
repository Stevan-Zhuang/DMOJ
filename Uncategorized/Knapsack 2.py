n_items, limit = [int(data) for data in input().split()]
data = [[int(data) for data in input().split()]
        for _ in range(n_items)]
weights, values = zip(*data)

max_value = sum(values)

dp = [0] * max_value + [float('inf')] * max_value
for item in range(n_items):
    for v_lim in reversed(range(max_value, max_value * 2)):
        dp[v_lim] = min(dp[v_lim], dp[v_lim - values[item]] + weights[item])

for value, weight in enumerate(reversed(dp)):
    if weight <= limit:
        print(max_value - value)
        break
