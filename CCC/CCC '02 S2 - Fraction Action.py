numer = int(input())
denom = int(input())

whole = numer // denom
numer -= whole * denom

a, b = numer, denom
while b:
  a, b = b, a % b
factor = a

if whole != 0:
  print(str(whole), end = " ")
if numer != 0:
  print(str(numer // factor) + "/" + str(denom // factor))
