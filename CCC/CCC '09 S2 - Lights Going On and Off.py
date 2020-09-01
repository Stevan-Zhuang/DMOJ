num_rows = int(input())
num_cols = int(input())

pattern = ["".join(input().split()) for row in range(num_rows)]
patterns = set()

for switch in range(num_rows):
    new_pattern = pattern.copy()
    for row in range(num_rows - switch, num_rows):
        new_pattern[row] = "".join("0" if new_pattern[row][col] == new_pattern[row - 1][col] else "1"
                                   for col in range(num_cols))
    patterns.add(new_pattern[-1])

print(len(patterns))
