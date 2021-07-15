n_vals, n_swaps = map(int, input().split())
arr = list(map(int, input().split()))
val2idx = {arr[idx]: idx for idx in range(n_vals)}
for idx in range(n_vals):
    if n_swaps == 0:
        break
    max_val = n_vals - idx
    if (arr[idx] == max_val):
        continue
    max_idx = val2idx[max_val]
    val2idx[arr[idx]] = max_idx
    val2idx[max_val] = idx
    arr[max_idx], arr[idx] = arr[idx], arr[max_idx]
    n_swaps -= 1
print(" ".join(map(str, arr)))
