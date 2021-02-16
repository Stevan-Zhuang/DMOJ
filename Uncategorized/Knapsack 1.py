n_items, limit = [int(data) for data in input().split()]

dp = [0] * (limit + 1)
for _ in range(n_items):
    weight, value = [int(data) for data in input().split()]
    for w_lim in reversed(range(weight, limit + 1)):
        dp[w_lim] = max(dp[w_lim], dp[w_lim - weight] + value)

print(dp[-1])
