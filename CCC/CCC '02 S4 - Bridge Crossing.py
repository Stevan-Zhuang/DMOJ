from math import inf

group_limit = int(input())
num_people = int(input())

names = []
times = []
for person in range(num_people):
    names.append(input())
    times.append(int(input()))

best_times = [0] + [inf] * num_people
shifts = [0] * num_people
for idx in range(num_people):
    max_time = 0
    for shift in range(group_limit):
        if idx + shift >= num_people:
            break
        max_time = max(max_time, times[idx + shift])
        if best_times[idx] + max_time < best_times[idx + shift + 1]:
            best_times[idx + shift + 1] = best_times[idx] + max_time
            shifts[idx + shift] = shift + 1

print("Total Time:", best_times[-1])

is_newline = [False] * num_people
idx = num_people - 1
while idx > 0:
    idx -= shifts[idx]
    is_newline[idx] = True

for name, newline in zip(names, is_newline):
    print(name, end="\n" if newline else " ")
