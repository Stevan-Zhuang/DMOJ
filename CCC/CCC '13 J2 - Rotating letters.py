letters = ["I", "O", "S", "H", "Z", "X", "N"]
sign = input()
if all(s in letters for s in sign):
  print("YES")
else:
  print("NO")
