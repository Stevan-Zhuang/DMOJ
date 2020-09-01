input = __import__('sys').stdin.readline

num_scores = int(input())
bi_tree = [0] + [0] * num_scores
ranks = [0] * num_scores
scores = sorted([(int(input()), idx)
                 for idx in range(num_scores)],
                reverse=True)
for idx, (score, score_idx) in enumerate(scores):
    ranks[score_idx] = idx + 1

def update(idx):
    while idx <= num_scores:
        bi_tree[idx] += 1
        idx += idx & -idx

def sum(idx):
    answer = 0
    while idx > 0:
        answer += bi_tree[idx]
        idx -= idx & -idx
    return answer

total = 0
for idx in range(num_scores):
    update(ranks[idx])
    total += sum(ranks[idx])

print(f"{total / num_scores:.2f}")
