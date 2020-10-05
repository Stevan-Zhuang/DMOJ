from collections import namedtuple
from itertools import permutations, combinations
from math import sqrt
input = __import__('sys').stdin.readline
Point = namedtuple('Point', ['x', 'y'])

num_points = int(input())
points = [Point(*[int(data) for data in input().split()])
          for _ in range(num_points)]

def pythag(p1, p2):
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5

def heron(a, b, c):
    s = (a + b + c)/2
    return sqrt(s*(s - a)*(s - b)*(s - c))

def circumcenter(p1, p2, p3):
    a = pythag(p1, p2)
    b = pythag(p2, p3)
    c = pythag(p3, p1)
    if any(sqrt(A ** 2 + B ** 2) < C
           for A, B, C in permutations([a, b, c], 3)):
        return max(a, b, c)
    return 2 * (a*b*c)/(4*heron(a, b, c))

max_distance = max(
    circumcenter(p1, p2, p3) for p1, p2, p3 in combinations(points, 3)
)
print(f"{max_distance:.2f}")
