ticket_prices = [int(input()) for i in range(4)]
target = int(input())

combos = []
for pink in range(target // ticket_prices[0] + 1):
  for green in range(target // ticket_prices[1] + 1):
    for red in range(target // ticket_prices[2] + 1):
      for orange in range(target // ticket_prices[3] + 1):
        if sum([pink, green, red, orange][i] * ticket_prices[i] for i in range(4)) == target:
          combos.append([pink, green, red, orange])

for combo in combos:
  print("# of PINK is {} # of GREEN is {} # of RED is {} # of ORANGE is {}".format(combo[0], combo[1], combo[2], combo[3]))
print("Total combinations is {}.".format(len(combos)))
print("Minimum number of tickets to print is {}.".format(min(sum(combo) for combo in combos)))
