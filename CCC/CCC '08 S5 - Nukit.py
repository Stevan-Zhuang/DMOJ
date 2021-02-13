memo = {}
def can_win(a, b, c, d):
    if (a, b, c, d) in memo:
        return memo[(a, b, c, d)]
    moves = [(a - 2, b - 1, c    , d - 2),
             (a - 1, b - 1, c - 1, d - 1),
             (a    , b    , c - 2, d - 1),
             (a    , b - 3, c    , d    ),
             (a - 1, b    , c    , d - 1)]
    moves = [move for move in moves if all(p >= 0 for p in move)]
    result = any(not can_win(*move) for move in moves)
    memo[(a, b, c, d)] = result
    return result

n_cases = int(input())
for _ in range(n_cases):
    a, b, c, d = [int(data) for data in input().split()]
    print("Patrick" if can_win(a, b, c, d) else "Roland")
