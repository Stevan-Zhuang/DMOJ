tine_len = int(input())
tine_space = int(input())
handle_len = int(input())

for _ in range(tine_len):
  print("*" + " " * tine_space + "*" + " " * tine_space + "*")
print("*" * (3 + tine_space * 2))
for _ in range(handle_len):
  print(" " * (tine_space + 1) + "*")
