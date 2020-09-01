numbers = ['1110111',
           '0010010',
           '1011101',
           '1011011',
           '0111010',
           '1101011',
           '1101111',
           '1010010',
           '1111111',
           '1111011']

num = int(input())

for i in range(7):
  if i % 3 == 0:
    print(" * * *" * int(numbers[num][i]))
  elif i == 1 or i == 4:
    for _ in range(3):
      print("*"  * int(numbers[num][i]), end = "")
      if int(numbers[num][i + 1]):
        if not int(numbers[num][i]):
          print(end = " ")
        print("     *")
      else:
        print("")
