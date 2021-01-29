input = __import__('sys').stdin.readline

num_tests, mark_total, mark_goal = [int(data) for data in input().split()]

goal = num_tests * mark_goal
total_time = 0
total_mark = 0

arr = [tuple(int(data) for data in input().split())
             for _ in range(num_tests)]
total_mark += sum(mark for mark, _ in arr)
arr = sorted((time, mark_total - mark) for mark, time in arr)

for time, incr in arr:
    total_time += time * incr
    total_mark += incr

    if total_mark >= goal:
        total_time -= (total_mark - goal) * time
        break

print(max(total_time, 0))
