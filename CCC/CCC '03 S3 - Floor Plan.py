flooring = int(input())
num_rows = int(input())
num_cols = int(input())
floor = [[char for char in input()] for row in range(num_rows)]

room_sizes = []
checked = []
for row in range(num_rows):
  for col in range(num_cols):
    room_size = 0
    queue = [[row, col]]
    for pos in queue:
      if floor[pos[0]][pos[1]] == '.' and not pos in checked:
        room_size += 1
        checked.append(pos)
        if pos[0] > 0: queue.append([pos[0] - 1, pos[1]])
        if pos[0] < num_rows - 1: queue.append([pos[0] + 1, pos[1]])
        if pos[1] > 0: queue.append([pos[0], pos[1] - 1])
        if pos[1] < num_cols - 1: queue.append([pos[0], pos[1] + 1])
    if room_size > 0:
      room_sizes.append(room_size)

room_sizes.sort(reverse = True)
num_rooms_floored = 0
while len(room_sizes) > 0 and flooring - room_sizes[0] >= 0:
  flooring -= room_sizes.pop(0)
  num_rooms_floored += 1

if num_rooms_floored == 1:
  print("{} room, {} square metre(s) left over".format(num_rooms_floored, flooring))
else:
  print("{} rooms, {} square metre(s) left over".format(num_rooms_floored, flooring))
