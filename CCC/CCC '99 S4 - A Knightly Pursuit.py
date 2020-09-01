from math import inf

knight_moves = {(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)}

for case in range(int(input())):
    num_rows, num_cols = int(input()), int(input())
    pawn_row, pawn_col = int(input()) - 1, int(input()) - 1
    knight_row, knight_col = int(input()) - 1, int(input()) - 1

    min_moves = [[inf] * num_cols for row in range(num_rows)]
    min_moves[knight_row][knight_col] = 0

    queue = [(knight_col, knight_row)]
    while queue:
        col, row = queue.pop(0)
        for move in knight_moves:
            new_col, new_row = col + move[0], row + move[1]
            if (    0 <= new_col < num_cols and 0 <= new_row < num_rows and
                    min_moves[new_row][new_col] == inf):
                min_moves[new_row][new_col] = min_moves[row][col] + 1
                queue.append((col + move[0], row + move[1]))

    num_moves = num_rows - 1 - pawn_row
    win_move = inf
    stalemate_move = inf
    for move in range(1, num_moves + 1):
        min_move = min_moves[pawn_row + move][pawn_col]
        if min_move <= move and move + 1 < num_moves and min_move % 2 == move % 2:
            win_move = min(move, win_move)
        if min_move <= move and min_move % 2 != move % 2:
            stalemate_move = min(move, stalemate_move)

    if win_move < inf:         print("Win in {} knight move(s).".format(win_move))
    elif stalemate_move < inf: print("Stalemate in {} knight move(s).".format(stalemate_move - 1))
    else:                      print("Loss in {} knight move(s).".format(num_moves - 1))
