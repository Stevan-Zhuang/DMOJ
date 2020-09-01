readings = [int(input()) for _ in range(4)]
if all(readings[i] < readings[i + 1] for i in range(3)):
  print("Fish Rising")
elif all(readings[i] > readings[i + 1] for i in range(3)):
  print("Fish Diving")
elif all(readings[i] == readings[i + 1] for i in range(3)):
  print("Fish At Constant Depth")
else:
  print("No Fish")
