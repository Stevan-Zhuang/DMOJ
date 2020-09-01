while True:
  word = input()
  if word == "X":
    break

  queued = [word]
  is_monkey_word = True
  while queued and is_monkey_word:
    partial = queued.pop(0)
    open_count = 0
    opens = []
    for i in reversed(range(len(partial))):
      if partial[i] == "S":
        if open_count == 0:
          opens.append(i)
        open_count += 1
      if partial[i] == "B":
        open_count -= 1
        if open_count == 0:
          queued.append(partial[i + 1: opens[0]])
          partial = partial[:i] + "A" + partial[opens.pop(0) + 1:]
    if not all(s == "A" for s in partial.split("N")):
      is_monkey_word = False
  
  if is_monkey_word:
    print("YES")
  else:
    print("NO")
