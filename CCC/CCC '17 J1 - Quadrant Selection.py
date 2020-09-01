quadrants = [[1, 4], [2, 3]]
pos = (int(input()), int(input()))
x, y = 0, 0
if pos[0] < 0: x += 1
if pos[1] < 0: y += 1
print(quadrants[x][y])
