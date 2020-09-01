import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
  cars = [int(input()) for n in range(int(input()))]
  branched = []
  can_slide = 1
  is_true = True

  while True:
    if len(cars) > 0 and cars[-1] == can_slide:
      cars.pop(-1)
      can_slide += 1
    elif len(branched) > 0 and branched[-1] == can_slide:
      branched.pop(-1)
      can_slide += 1
    elif len(cars) > 0:
      branched.append(cars.pop(-1))
    elif len(branched) == 0:
      break
    else:
      is_true = False
      break

  if is_true:
    print('Y')
  else:
    print('N')
