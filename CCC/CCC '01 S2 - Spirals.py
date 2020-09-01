pos = [4, 4]
count = 0
side_len = 1
dist = 1

spiral = [["" for col in range(10)] for row in range(10)]
for num in range(int(input()), int(input()) + 1):
  spiral[pos[1]][pos[0]] = str(num)
  count += 1
  if count <= side_len: pos[1] += dist
  elif count > side_len: pos[0] += dist
  if count == side_len * 2:
    count = 0
    side_len += 1
    dist = -dist

print("\n".join(" ".join(row).strip() for row in spiral
                if not all(num == "" for num in row)))
