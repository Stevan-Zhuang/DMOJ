intersect_dirs = {'-': [(1, 0), (-1, 0)],
                  '|': [(0, 1), (0, -1)],
                  '+': [(1, 0), (0, 1), (-1, 0), (0, -1)]}

for case in range(int(input())):
    num_rows = int(input())
    num_cols = int(input())

    maze = [input() for row in range(num_rows)]
    min_counts = [[-1 for col in range(num_cols)] for row in range(num_rows)]

    queue = [(0, 0, 1)]
    while queue:
        col, row, count = queue.pop(0)

        if maze[row][col] == '*':
            continue
        if min_counts[row][col] != -1 and count >= min_counts[row][col]:
            continue
        if min_counts[row][col] == -1 or count < min_counts[row][col]:
            min_counts[row][col] = count
        if col + 1 == num_cols and row + 1 == num_rows:
            break

        for dir in intersect_dirs[maze[row][col]]:
            new_col, new_row = col + dir[0], row + dir[1]
            if (    new_col < num_cols and new_col >= 0 and
                    new_row < num_rows and new_row >= 0):
                queue.append((new_col, new_row, count + 1))

    print(min_counts[-1][-1])
