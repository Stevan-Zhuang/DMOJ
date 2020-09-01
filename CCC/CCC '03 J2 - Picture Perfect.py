while True:
  photo_num = int(input())
  if photo_num == 0:
    break
  for i in range(int(photo_num ** 0.5), 0, -1):
    if photo_num % i == 0:
      print("Minimum perimeter is",
            (i + photo_num//i) * 2,
            "with dimensions", i, "x", photo_num//i)
      break
