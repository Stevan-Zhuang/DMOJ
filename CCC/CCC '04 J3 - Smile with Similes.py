adjs = []
nouns = []
adj_num = int(input())
noun_num = int(input())
for _ in range(adj_num):
  adjs.append(input())
for _ in range(noun_num):
  nouns.append(input())
for adj in adjs:
  for noun in nouns:
    print(adj, "as", noun)
