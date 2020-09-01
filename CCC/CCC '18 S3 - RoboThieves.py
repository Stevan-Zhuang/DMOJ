num_rows, num_cols = [int(data) for data in input().split()]

grid = []
start_pos = (0, 0)
min_steps = [[-1 for col in range(num_cols)] for row in range(num_rows)]

is_invalid = [[False for col in range(num_cols)] for row in range(num_rows)]

for row in range(num_rows):
    cur_row = input()
    for col in range(num_cols):
        if cur_row[col] == "S": start_pos = (col, row)
        if cur_row[col] == "W": is_invalid[row][col] = True
    grid.append(cur_row)


orients = [(-1, 0), (1, 0), (0, -1), (0, 1)]
conveyers = "LRUD"

for row in range(num_rows):
    for col in range(num_cols):
        if grid[row][col] == "C":
            for orient in orients:
                temp_col = col
                temp_row = row
                while grid[temp_row][temp_col] != "W":
                    if not grid[temp_row][temp_col] in conveyers:
                        is_invalid[temp_row][temp_col] = True
                    temp_col += orient[0]
                    temp_row += orient[1]

conveyer_paths = {}
def set_conveyers(path):
    col, row = path[-1]
    if is_invalid[row][col]:
        return None
    if not grid[row][col] in conveyers:
        return (col, row)

    orient = orients[conveyers.index(grid[row][col])]
    if (col + orient[0], row + orient[1]) in path:
        return None
    result = set_conveyers(path + [(col + orient[0], row + orient[1])])
    if result is None:
        is_invalid[row][col] = True
    else:
        conveyer_paths[(col, row)] = result
    return result

for row in range(num_rows):
    for col in range(num_cols):
        if grid[row][col] in conveyers and not is_invalid[row][col]:
            set_conveyers([(col, row)])


queue = [(start_pos, 0)]
while queue:
    data = queue.pop(0)
    col, row = data[0]
    steps_taken = data[1]

    if is_invalid[row][col]:
        continue

    if min_steps[row][col] != -1 and steps_taken >= min_steps[row][col]:
        continue
    if min_steps[row][col] == -1 or steps_taken < min_steps[row][col]:
        min_steps[row][col] = steps_taken

    if grid[row][col] in conveyers:
        queue.append((conveyer_paths[(col, row)], steps_taken))
        continue

    for orient in orients:
        queue.append(((col + orient[0], row + orient[1]), steps_taken + 1))


for row in range(num_rows):
    for col in range(num_cols):
        if grid[row][col] == ".":
            print(min_steps[row][col])
