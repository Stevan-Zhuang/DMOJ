yodel_num, round_num = [int(s) for s in input().split()]
scores = [[int(s) for s in input().split()]
          for _ in range(round_num)]

high_score = max(sum(scores[j][i] for j in range(round_num))
                 for i in range(yodel_num))

for i in range(yodel_num):
  if sum(scores[j][i] for j in range(round_num)) == high_score:
    total_scores = [0] * yodel_num
    ranks = []
    for j in range(round_num):
      for k in range(yodel_num):
        total_scores[k] += scores[j][k]
      ranks.append(sorted(total_scores, reverse = True).index(total_scores[i]) + 1)
    
    print("Yodeller {} is the TopYodeller: score {}, worst rank {}".format(i + 1, high_score, max(ranks)))
