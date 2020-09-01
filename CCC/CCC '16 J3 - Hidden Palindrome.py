palindromes = []
word = input()
for start in range(len(word)):
  for length in range(len(word) - start):
    string = word[start: start + length + 1]
    if string == string[::-1]:
      palindromes.append(string)
print(max(len(s) for s in palindromes))
