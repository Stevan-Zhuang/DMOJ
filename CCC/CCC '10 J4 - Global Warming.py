while True:
  case_data = [int(s) for s in input().split()]
  if case_data == [0]: break
  seq_len, temps = case_data[0], case_data[1:]
  changes = [temps[i + 1] - temps[i] for i in range(seq_len - 1)]
  for i in range(seq_len - 1):
    if all(changes[j: j + i + 1] == changes[:i + 1][:len(changes[j: j + i + 1])] for j in range(0, seq_len - 1, i + 1)):
      print(i + 1)
      break
  if seq_len == 1:
    print(0)
