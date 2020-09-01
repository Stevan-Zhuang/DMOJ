width = int(input())
height = int(input())

product = width * height
print(product // 4, end=".")
print(["00", "25", "50", "75"][product % 4])
