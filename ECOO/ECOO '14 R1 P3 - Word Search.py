alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for case in range(5):
  num_rows, num_cols = [int(s) for s in input().split()]
  word_search = [input() for row in range(num_rows)]
  clue_words = ["".join(char for char in input() if char in alphabet)
                for word in range(int(input()))]
  circled = [[False for col in range(num_cols)] for row in range(num_rows)]
  for word in clue_words:
    word_found = False
    for row in range(num_rows):
      for col in range(num_cols):
        if word_search[row][col] == word[0]:
          for dir in [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]:
            if all(0 <= row + dir[0] * i < num_rows and
                   0 <= col + dir[1] * i < num_cols and
                   word_search[row + dir[0] * i][col + dir[1] * i] == word[i] for i in range(1, len(word))):
              word_found = True
              for i in range(len(word)):
                circled[row + dir[0] * i][col + dir[1] * i] = True
              break
        if word_found: break
      if word_found: break
  
  print("".join(word_search[row][col] for row in range(num_rows) for col in range(num_cols) if not circled[row][col]))
