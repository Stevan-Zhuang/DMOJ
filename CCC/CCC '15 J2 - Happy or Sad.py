message = input()

num_happy = 0
num_sad = 0

for idx in range(len(message) - 2):
    substr = message[idx: idx + 3]
    if substr == ":-)": num_happy += 1
    if substr == ":-(": num_sad += 1

if num_happy == 0 and num_sad == 0:
    print("none")
elif num_happy > num_sad:
    print("happy")
elif num_sad > num_happy:
    print("sad")
else:
    print("unsure")
