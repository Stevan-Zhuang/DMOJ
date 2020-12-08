input = __import__("sys").stdin.readline

num_slice = int(input())
widths = [int(data) for data in input().split()]
heights = [int(data) for data in input().split()]

width_sums = [0, 0, 0]
for i, a in enumerate(widths):
    width_sums[(i + 2) % 3] += a

areas = [0, 0, 0]
for j, b in enumerate(heights):
    for c in range(3):
        areas[(j + c) % 3] += width_sums[c] * b
    
print(" ".join(str(data) for data in areas))
