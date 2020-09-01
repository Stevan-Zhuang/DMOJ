num = int(input())
measurements = [int(s) for s in input().split()]
measurements.sort()

low_tides = []
high_tides = []

for i in range((num - 1) // 2, -1, -1):
  low_tides.append(measurements[i])
for i in range((num - 1) // 2 + 1, num):
  high_tides.append(measurements[i])

measurements[:: 2] = low_tides
measurements[1:: 2] = high_tides

print(" ".join(str(i) for i in measurements))
