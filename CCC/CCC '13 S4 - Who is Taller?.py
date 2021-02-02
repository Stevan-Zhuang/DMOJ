import sys
input = sys.stdin.readline

from collections import deque

num_people, num_comparisons = [int(data) for data in input().split()]

network = [[] for people in range(num_people + 1)]
for comparision in range(num_comparisons):
    person_x, person_y = [int(data) for data in input().split()]
    network[person_x].append(person_y)

def is_taller(person_x, person_y):
    visited = [False] * (num_people + 1)
    visited[person_x] = True

    queue = deque([person_x])
    while queue:
        person = queue.popleft()
        if person == person_y:
            return True
        for other_person in network[person]:
            if not visited[other_person]:
                queue.append(other_person)
                visited[other_person] = True

person_x, person_y = [int(data) for data in input().split()]

if is_taller(person_x, person_y):   print("yes")
elif is_taller(person_y, person_x): print("no")
else:                               print("unknown")
