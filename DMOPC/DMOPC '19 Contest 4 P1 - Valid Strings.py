for case in range(int(input())):
  line = input()
  open_count = 0
  is_valid = True
  for s in line:
    if s == "(": open_count += 1
    if s == ")": open_count -= 1
    if open_count < 0:
      is_valid = False
      break
  if open_count != 0:
    is_valid = False

  if is_valid:
    print("YES")
  else:
    print("NO")
