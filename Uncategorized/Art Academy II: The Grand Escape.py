import sys
input = sys.stdin.readline

"""
>>> a = 2654435761
>>> m = -4294967296
>>> x0, x1, y0, y1 = 0, 1, 1, 0
>>> while a != 0:
...     (q, a), m = divmod(m, a), a
...     y0, y1 = y1, y0 - q * y1
...     x0, x1 = x1, x0 - q * x1
>>> x0
244002641
"""

num_paintings, num_greatest = [int(data) for data in input().split()]
print(sum(sorted([(244002641 * int(input())) % 4294967296 for painting in range(num_paintings)], reverse=True)[:num_greatest]))
