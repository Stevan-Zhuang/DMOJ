import sys
input = sys.stdin.readline

num_students = int(input())
class_total = sum(int(input()) for _ in range(num_students))

for _ in range(int(input())):
  num_students += 1
  class_total += int(input())
  print("{:.3f}".format(class_total / num_students))
