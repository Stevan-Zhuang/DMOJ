k = int(input())
D = {}
for _ in range(k):
    c, s = input().split()
    D[c] = s

m = ""
b = input()
while len(b) > 0:
    for c, s in D.items():
        if s == b[:len(s)]:
            m += c
            b = b[len(s):]
            break

print(m)
