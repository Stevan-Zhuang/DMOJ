spirals = []
case_num = int(input())
for case in range(case_num):
  pos = [4, 4]
  count = 0
  s_len = 1
  dis = 1
  spiral = [["" for _ in range(10)] for _ in range(10)]

  start, end = [int(s) for s in input().split()]
  for i in range(start, end + 1):
    spiral[pos[1]][pos[0]] = str(i)

    count += 1
    if count <= s_len: pos[1] += dis 
    if count > s_len: pos[0] += dis
    if count == s_len * 2:
      count = 0
      s_len += 1
      dis = -dis

  spiral = [row for row in spiral if not all(s == "" for s in row)]
  for i in reversed(range(len(spiral[0]))):
    if all(row[i] == "" for row in spiral):
      for row in spiral:
        row.pop(i)

  widths = []
  for i in range(len(spiral[0])):
      widths.append(max(len(s) for s in [row[i] for row in spiral]))

  spirals.append("\n".join(" ".join(" " * (widths[i] - len(row[i])) + row[i]
                                    for i in range(len(row)))
                           for row in spiral))
                           
print("\n\n".join(spirals))
