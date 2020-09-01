input = __import__('sys').stdin.readline
num_cols, num_rows, max_size = [int(data) for data in input().split()]
grid = [[int(data) for data in input().split()] for _ in range(num_rows)]

prefix_sum = [[0] * (num_cols + 1) for _ in range(num_rows + 1)]
for row in range(1, num_rows + 1):
    for col in range(1, num_cols + 1):
        prefix_sum[row][col] = (prefix_sum[row - 1][col]
                                + prefix_sum[row][col - 1]
                                + grid[row - 1][col - 1]
                                - prefix_sum[row - 1][col - 1])

def get_scales(x1, y1, x2, y2):
    return (prefix_sum[y2][x2]
            - prefix_sum[y1][x2]
            - prefix_sum[y2][x1]
            + prefix_sum[y1][x1])

max_scales = 0
for width in range(1, num_cols + 1):
    height = max_size // width
    if width * height <= max_size:
        for row in range(num_rows - height + 1):
            for col in range(num_cols - width + 1):
                scales = get_scales(col, row, col + width, row + height)
                max_scales = max(scales, max_scales)
                
print(max_scales)
