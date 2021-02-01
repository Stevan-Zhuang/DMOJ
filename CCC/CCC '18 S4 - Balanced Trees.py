from math import sqrt
input = __import__('sys').stdin.readline

memo = {}
def f(n):
    if n < 2:
        return 1
    if n in memo:
        return memo[n]
    s = 0
    sq_n = int(sqrt(n))
    # praise the editorial
    for j in range(1, sq_n + 1):
        k = n // j
        s += (k - (n // (j + 1))) * f(j)
        if j >= 2 and k > sq_n:
            s += f(k)
    memo[n] = s
    return s

print(f(int(input())))
