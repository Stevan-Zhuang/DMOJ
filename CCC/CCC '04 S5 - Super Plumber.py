input = __import__('sys').stdin.readline

num_rows, num_cols = [int(data) for data in input().split()]
while (num_rows, num_cols) != (0, 0):
    grid = [input() for _ in range(num_rows)]
    values = [[int(grid[row][col])
               if grid[row][col] in "123456789" else 0
               for col in range(num_cols)]
              for row in range(num_rows)]

    dp_prev = [-1] * num_rows
    dp_cur = [-1] * num_rows
    
    dp_prev[-1] = 0
    for col in range(num_cols):
        for row in range(num_rows):
            if dp_prev[row] != -1:
                start = dp_prev[row]
                for shift in range(row + 1):
                    if grid[row - shift][col] == "*":
                        break
                    start += values[row - shift][col]
                    dp_cur[row - shift] = max(start, dp_cur[row - shift])
                start = dp_prev[row]
                for shift in range(num_rows - row):
                    if grid[row + shift][col] == "*":
                        break
                    start += values[row + shift][col]
                    dp_cur[row + shift] = max(start, dp_cur[row + shift])

        dp_prev = dp_cur
        dp_cur = [-1] * num_rows
    
    print(dp_prev[-1])

    num_rows, num_cols = [int(data) for data in input().split()]
