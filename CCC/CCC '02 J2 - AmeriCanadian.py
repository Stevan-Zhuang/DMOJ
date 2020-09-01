word = input()
while word != "quit!":
  if len(word) > 4 and word[-2:] == "or" and not word[-3] in ["a","e","i","o","u","y"]:
    print(word[:-2] + "our")
  else:
    print(word)
  word = input()
