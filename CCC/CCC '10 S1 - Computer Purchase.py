n = int(input())
C = []
for _ in range(n):
    s, R, S, D = input().split()
    R, S, D = int(R), int(S), int(D)
    C.append((2*R + 3*S + D, s))
C.sort(key=lambda L: L[1])
C.sort(key=lambda L: L[0], reverse=True)
if len(C) == 0:
    print()
elif len(C) == 1:
    print(C[0][1])
else:
    print(C[0][1])
    print(C[1][1])
