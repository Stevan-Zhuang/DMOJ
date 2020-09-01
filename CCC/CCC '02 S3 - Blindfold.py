grid_size = [int(input()), int(input())][::-1]
grid = [[tile for tile in input()]
        for row in range(grid_size[1])]

move_num = int(input())
moves = [input() for _ in range(move_num)] 
faces = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for row in range(grid_size[1]):
  for tile in range(grid_size[0]):
    if grid[row][tile] != "X":
      for face in faces:
        pos = [tile, row]
        possible = True
        for move in moves:
          if move == 'F':
            if (all(pos[i] + face[i] >= 0 for i in range(2))
                and all(pos[i] + face[i] < grid_size[i] for i in range(2))
                and grid[pos[1] + face[1]][pos[0] + face[0]] != "X"):
              pos = [pos[i] + face[i] for i in range(2)]
            else:
              possible = False
              break
          elif move == 'L':
            face = faces[(faces.index(face) - 1) % 4]
          elif move == 'R':
            face = faces[(faces.index(face) + 1) % 4]
        if possible:
          grid[pos[1]][pos[0]] = "*"

for row in grid:
  print("".join(row))
