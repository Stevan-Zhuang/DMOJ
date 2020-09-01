for case in range(int(input())):
  seq_len = int(input())
  seq_x = [int(s) for s in input().split()]
  seq_y = [int(s) for s in input().split()]
  print("The maximum distance is {}".format(max(j - i if j >= i and seq_y[j] >= seq_x[i] else 0 for i in range(seq_len) for j in range(seq_len))))
