square = 1
while True:
  move = int(input())
  if move == 0:
    print("You Quit!")
    break
  if square + move <= 100:
    square += move

  if square == 54: square = 19
  if square == 90: square = 48
  if square == 99: square = 77
  if square == 9: square = 34
  if square == 40: square = 64
  if square == 67: square = 86

  print("You are now on square", square)
  if square == 100:
    print("You Win!")
    break
