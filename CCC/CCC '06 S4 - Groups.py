while True:
    group_size = int(input())
    if group_size == 0:
        break

    elements = [row + 1 for row in range(group_size)]
    group = [[int(element) for element in input().split()] for row in range(group_size)]

    if not all(group[x][group[y][z] - 1] == group[group[x][y] - 1][z]
               for z in range(group_size)
               for y in range(group_size)
               for x in range(group_size)):
        print("no")
        continue

    identity = 0
    for row in range(group_size):
        if group[row] == elements and [group[row][col] for col in range(group_size)] == elements:
            identity = row + 1
    if identity == 0:
        print("no")
        continue

    if not all(any(group[row][col] == identity and group[col][row] == identity
                   for col in range(group_size))
               for row in range(group_size)):
        print("no")
        continue

    print("yes")
