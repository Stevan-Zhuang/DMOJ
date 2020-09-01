def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for case in range(int(input())):
  n = int(input())
  for a in range(2, n * 2):
    b = n * 2 - a
    if is_prime(a) and is_prime(b):
      print(a, b)
      break
