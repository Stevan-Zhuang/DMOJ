def get_possible_moves(num_a, num_b, num_c, num_d):
    possible_moves = {(num_a - 2, num_b - 1, num_c,     num_d - 2),
                      (num_a - 1, num_b - 1, num_c - 1, num_d - 1),
                      (num_a,     num_b,     num_c - 2, num_d - 1),
                      (num_a,     num_b - 3, num_c,     num_d),
                      (num_a - 1, num_b,     num_c,     num_d - 1)}

    possible_moves = {(num_a, num_b, num_c, num_d) for num_a, num_b, num_c, num_d in possible_moves
                      if num_a >= 0 and num_b >= 0 and num_c >= 0 and num_d >= 0}

    return possible_moves

cache = {}

def always_wins(particles, moves_made = 0):
    if (particles, moves_made % 2) in cache:
        return cache[(particles, moves_made % 2)]

    num_a, num_b, num_c, num_d = particles
    possible_moves = get_possible_moves(num_a, num_b, num_c, num_d)
    if len(possible_moves) == 0:
        return moves_made % 2 == 1

    if moves_made % 2 == 0:
        result = any(always_wins(move, moves_made + 1) for move in possible_moves)
        cache[(particles, 0)] = result
        return result
    if moves_made % 2 == 1:
        result = all(always_wins(move, moves_made + 1) for move in possible_moves)
        cache[(particles, 1)] = result
        return result

for case in range(int(input())):
    particles = tuple(int(data) for data in input().split())
    print("Patrick" if always_wins(particles) else "Roland")
