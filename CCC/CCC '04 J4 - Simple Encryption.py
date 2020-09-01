alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

keyword = input()
message = [l for l in input() if l in alphabet]

for l in range(len(keyword)):
  for i in range(l, len(message), len(keyword)):
    message[i] = alphabet[(alphabet.index(message[i])
                          + alphabet.index(keyword[l])) % 26]

print("".join(message))
