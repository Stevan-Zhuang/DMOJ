x = int(input())
m = int(input())
a = False
for n in range(1, m):
  if x * n % m == 1:
    print(n)
    a = True
if not a:
  print("No such integer exists.")
