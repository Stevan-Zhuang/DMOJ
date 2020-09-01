sequence = input()
hor_flip = sequence.count("H") % 2
ver_flip = sequence.count("V") % 2
grid = [["1", "2"], ["3", "4"]]
if hor_flip: grid = [row for row in grid[:: -1]]
if ver_flip: grid = [row[:: -1] for row in grid]
for row in grid:
  print(" ".join(row))
