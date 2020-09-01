import sys
from bisect import bisect_left
input = sys.stdin.readline

num_gates = int(input())
num_planes = int(input())

undocked = [gate + 1 for gate in range(num_gates)]

def binary_search(max_dock):
    idx = bisect_left(undocked, max_dock)
    if idx == len(undocked) or undocked[idx] > max_dock and idx > 0:
        return idx - 1
    if undocked[idx] == max_dock:
        return idx
    raise ValueError

for plane in range(num_planes):
    max_dock = int(input())
    try:    undocked.pop(binary_search(max_dock))
    except: break

print(num_gates - len(undocked))
