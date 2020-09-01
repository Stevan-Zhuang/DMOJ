vowels = "aeiou"

case_num = int(input())
for _ in range(case_num):
  words = [input().split()[-1].lower() for _ in range(4)]
  syls = []
  for word in words:
    vowel = 0
    for i in range(len(word)):
      if word[i] in vowels:
        vowel = i
    syls.append(word[vowel:])

  if syls[0] == syls[1] == syls[2] == syls[3]:
    print("perfect")
  elif syls[0] == syls[1] and syls[2] == syls[3]:
    print("even")
  elif syls[0] == syls[2] and syls[1] == syls[3]:
    print("cross")
  elif syls[0] == syls[3] and syls[1] == syls[2]:
    print("shell")
  else:
    print("free")
