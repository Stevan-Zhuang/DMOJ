input = __import__('sys').stdin.readline

n_people = int(input())

walk_left = 0
walk_right = 0
cur_time = 0
prev_pos = 0

people = []
for _ in range(n_people):
    p, w, d = [int(data) for data in input().split()]
    people.append((p + d, w, 0))
    if p - d > 0:
        people.append((p - d, w, 1))
        cur_time += (p - d) * w
        walk_right += w

people.sort()

best_time = float('inf')
for pos, walk, left in people:
    best_time = min(best_time, cur_time)

    dist = pos - prev_pos
    
    cur_time += dist * walk_left
    cur_time -= dist * walk_right
    best_time = min(best_time, cur_time)

    prev_pos = pos
    if not left:
        walk_left += walk
    if left:
        walk_right -= walk

print(best_time)
