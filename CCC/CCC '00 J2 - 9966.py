can_flip = "01869"
flipped = "01896"

count = 0
for num in range(int(input()), int(input()) + 1):
  num = str(num)
  if all(num[let] in can_flip
         and num[-let - 1] == flipped[can_flip.index(num[let])]
         for let in range(len(num) // 2 + (len(num) % 2 > 0))):
    count += 1

print(count)
