space_num = int(input())

today = input()
yesterday = input()

same_sum = 0

for i in range(space_num):
  if today[i] == yesterday[i] == "C":
    same_sum += 1

print(same_sum)
