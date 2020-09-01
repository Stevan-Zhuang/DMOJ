from math import inf
from collections import defaultdict

network = dict()
num_students = int(input())
for num_assigns in range(num_students):
    student, friend = input().split()
    network[student] = friend

while True:
    student1, student2 = input().split()
    if student1 == '0' and student2 == '0':
        break

    min_separation = {key: inf for key in network}
    queue = [(network[student1], 0)]
    while queue:
        cur_student, separation = queue.pop()
        if separation >= min_separation[cur_student]:
            continue
        min_separation[cur_student] = separation
        if cur_student == student1:
            break
        queue.append((network[cur_student], separation + 1))

    print("Yes {}".format(min_separation[student2]) if min_separation[student2] != inf else "No")
