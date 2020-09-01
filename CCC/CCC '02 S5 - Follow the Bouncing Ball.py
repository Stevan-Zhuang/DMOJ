screen_x, screen_y = int(input()), int(input())
start_x, start_y = int(input()), int(input())
slope = start_y / (screen_x - start_x)

def round_nearest(num, multiple):
    return multiple * (int((num - multiple / 2) / multiple) + 1)

inf = float('inf')

bounce_count = inf
limit = 100000
for bounce_y in range(1, limit):
    ball_x = screen_y * bounce_y / slope + start_x

    close_x = abs(ball_x - round_nearest(ball_x, screen_x))
    if close_x < 5:
        bounce_x = int(ball_x / screen_x)

        bounce_y -= 1
        if close_x == 0:
            bounce_x -= 1

        bounce_count = min(bounce_y + bounce_x, bounce_count)
        break

for bounce_x in range(1, limit):
    ball_y = (screen_x * bounce_x - start_x) * slope

    close_y = abs(ball_y - round_nearest(ball_y, screen_y))
    if close_y < 5:
        bounce_y = int(ball_y / screen_y)

        bounce_x -= 1
        if close_y == 0:
            bounce_y -= 1

        bounce_count = min(bounce_y + bounce_x, bounce_count)
        break

print(bounce_count if bounce_count < inf else 0)
