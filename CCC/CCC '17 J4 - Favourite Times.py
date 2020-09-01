time = [12, 0, 0]
count = 0
duration = int(input())

cycles = duration // 720
minutes = duration % 720

for _ in range(minutes):
  time[2] += 1
  if time[2] == 10:
    time[1] += 1
    time[2] = 0
  if time[1] == 6:
    time[0] += 1
    time[1] = 0
  if time[0] == 13:
    time[0] = 1

  sequence = ("".join(str(i) for i in time))
  constant = int(sequence[-1]) - int(sequence[-2])
  if all(int(sequence[i + 1]) - int(sequence[i]) == constant
         for i in range(len(sequence) - 2)):
    count += 1
count += cycles * 31

print(count)
