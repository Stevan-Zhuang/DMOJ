flower_num = int(input())
flowers = [[int(s) for s in input().split()]
            for _ in range(flower_num)]

while (not all(all(flowers[i][j] < flowers[i][j + 1]
                   for j in range(len(flowers[0]) - 1))
               for i in range(len(flowers)))
    or not all(all(flowers[j][i] < flowers[j + 1][i]
                   for j in range(len(flowers[0]) - 1))
               for i in range(len(flowers)))):

  flowers = [[flowers[j][i] for j in range(len(flowers))][::-1]
              for i in range(len(flowers))]

for row in flowers:
  print(" ".join(str(i) for i in row))
