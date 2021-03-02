i = int(input())
while True:
    i += 1
    year = str(i)
    if len(set(year)) == len(year):
        print(i)
        break
