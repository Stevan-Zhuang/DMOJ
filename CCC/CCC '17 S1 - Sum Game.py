game_num = int(input())

swift = [int(s) for s in input().split()]
semaphore = [int(s) for s in input().split()]

swift_num = 0
semaphore_num = 0
max_same = 0

for i in range(game_num):
  swift_num += swift[i]
  semaphore_num += semaphore[i]
  if swift_num == semaphore_num:
    max_same = i + 1

print(max_same)
