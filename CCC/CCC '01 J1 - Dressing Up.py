height = int(input())

for i in range(height):
    if i > height//2: i = abs(i - height + 1)
    print("*" * (i * 2 + 1) + " " * (abs(2 + i * 4 - height * 2)) + "*" * (i * 2 + 1))
