suits = ['C', 'D', 'H', 'S']
suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
cards = [[], [], [], []]
values = {'A': 4, 'K': 3, 'Q': 2, 'J': 1}
extra_values = {0: 3, 1: 2, 2: 1}

string = input()
suit = -1
for sub_s in string:
  if sub_s in suits:
    suit += 1
  else:
    cards[suit].append(sub_s)

print("Cards Dealt              Points")
total = 0
for suit in range(len(suits)):
  space = 30
  suit_total = 0
  print(suit_names[suit], end = " ")
  space -= len(suit_names[suit])
  for card in cards[suit]:
    print(card, end = " ")
    space -= len(card) + 1
    suit_total += values.get(card, 0)
  suit_total += extra_values.get(len(cards[suit]), 0)
  space -= len(str(suit_total))
  print(" " * space + str(suit_total))
  total += suit_total
print(" " * (25 - len(str(total))) + "Total", total)
