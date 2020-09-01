num = int(input())
vills = [int(input())
            for _ in range(num)]
vills.sort()

print(min(vills[i + 1]/2 - vills[i - 1]/2
          for i in range(1, num - 1)))
