n_pieces = int(input())
heights = [int(data) for data in input().split()]
widths = [int(data) for data in input().split()]
print(sum((heights[idx] + heights[idx + 1]) * widths[idx] / 2
          for idx in range(n_pieces)))
