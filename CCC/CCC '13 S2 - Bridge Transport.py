import sys
input = sys.stdin.readline

count = 0
cars = []
max_weight = int(input())
for car in range(int(input())):
  cars.append(int(input()))
  if len(cars) > 4:
    cars = cars[1:]
  if sum(cars) > max_weight:
    break
  else:
    count += 1

print(count)
