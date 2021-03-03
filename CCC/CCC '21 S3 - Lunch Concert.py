n_people = int(input())
data = [[int(data) for data in input().split()]
        for _ in range(n_people)]
people = []
for p, w, d in data:
    people.append((p - d, w, 1))
    people.append((p + d, w, 0))
people.sort()
del data

best_time = float('inf')
for cur, (pos, walk, left) in enumerate(people):
    if cur == 0:
        total_walk_left = 0
        total_walk_right = sum(w for p, w, l in people if l and pos < p)

        cur_time = sum((p - pos) * w for p, w, l in people if l)
        best_time = min(best_time, cur_time)
    else:
        dist = (people[cur][0] - people[cur - 1][0])
        
        cur_time += dist * total_walk_left
        cur_time -= dist * total_walk_right
        best_time = min(best_time, cur_time)

        if not left: total_walk_left += walk
        if left: total_walk_right -= walk

print(best_time)
