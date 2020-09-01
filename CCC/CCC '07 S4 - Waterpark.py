from collections import defaultdict

slides = defaultdict(set)
num_slides = int(input())
while True:
    start, end = input().split()
    if start == '0' and end == '0':
        break
    slides[start].add(end)

last_slide = str(num_slides)
memo = {}
def count_paths(cur_slide):
    if cur_slide in memo:
        return memo[cur_slide]
    if cur_slide == last_slide:
        return 1
    result = sum(count_paths(slide) for slide in slides[cur_slide])
    memo[cur_slide] = result
    return result

print(count_paths('1'))
