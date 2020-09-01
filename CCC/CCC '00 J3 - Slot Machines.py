quarters = int(input())
last_paid = [int(input()), int(input()), int(input())]

pay_time = [35, 100, 10]
payout = [30, 60, 9]

plays = 0
while quarters > 0:
  for slot in range(3):
    plays += 1
    quarters -= 1
    last_paid[slot] += 1
    if last_paid[slot] % pay_time[slot] == 0:
      quarters += payout[slot]
    if quarters == 0:
      break

print("Martha plays {} times before going broke.".format(plays))
