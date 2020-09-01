fav_team = int(input()) - 1
num_games_played = int(input())

def tally(scores, team_a, team_b, score_a, score_b):
    temp_scores = scores.copy()
    if score_a > score_b:
        temp_scores[team_a] += 3
    if score_a < score_b:
        temp_scores[team_b] += 3
    if score_a == score_b:
        temp_scores[team_a] += 1
        temp_scores[team_b] += 1
    return temp_scores

scores = [0] * 4
games_played = []
for _ in range(num_games_played):
    team_a, team_b, score_a, score_b = [int(s) for s in input().split()]
    scores = tally(scores, team_a - 1, team_b - 1, score_a, score_b)
    games_played.append((team_a - 1, team_b - 1))

remaining_games = [game for game in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
                   if game not in games_played]

chances = 0
queue = [[remaining_games, scores]]
while queue:
    partial_games, partial_scores = queue.pop(0)
    if len(partial_games) == 0:
        if all(partial_scores[fav_team] > partial_scores[i] for i in range(4) if i != fav_team):
            chances += 1

    else:
        team_a = partial_games[0][0]
        team_b = partial_games[0][1]
        queue.append([partial_games[1:], tally(partial_scores, team_a, team_b, 1, 0)])
        queue.append([partial_games[1:], tally(partial_scores, team_a, team_b, 0, 1)])
        queue.append([partial_games[1:], tally(partial_scores, team_a, team_b, 0, 0)])

print(chances)
