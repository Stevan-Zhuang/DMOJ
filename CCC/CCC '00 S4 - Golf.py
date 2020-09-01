goal = int(input())
clubs = sorted([int(input()) for club in range(int(input()))], reverse=True)

min_strokes = 0
cache = {}
def can_sum(goal, num_clubs = 0):
    if goal in cache:
        return cache[goal]
    if goal < 0:
        return False
    if goal == 0:
        global min_strokes
        min_strokes = num_clubs
        return True
    result = any(can_sum(goal - club, num_clubs + 1) for club in clubs)
    cache[goal] = result
    return result

if can_sum(goal):
    print("Roberta wins in {} strokes.".format(min_strokes))
else:
    print("Roberta acknowledges defeat.")
