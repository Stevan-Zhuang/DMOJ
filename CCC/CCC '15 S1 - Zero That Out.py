import sys
input = sys.stdin.readline

earnings = []
for _ in range(int(input())):
  num = int(input())
  if num == 0: earnings.pop()
  else: earnings.append(num)

print(sum(earnings))
