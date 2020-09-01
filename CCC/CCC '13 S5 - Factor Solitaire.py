input = __import__('sys').stdin.readline
c = int(input())
p = 0
while c != 1:
    for b in range(2, c + 1):
        if c / b % 1 == 0:
            a = c // b
            if c - a >= 1:
                c -= a
                p += b - 1
                break
print(p)
