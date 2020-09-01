max_seq_len = int(input())
seq_len = int(input())
seq_a = [input() for _ in range(seq_len)]
seq_b = [input() for _ in range(seq_len)]

def seq_exists(seq_ints = [], partial_a = "", partial_b = ""):
    if partial_a == partial_b and len(seq_ints) > 0:
        print(len(seq_ints))
        for i in seq_ints:
            print(i + 1)
        return True

    min_len = min(len(partial_a), len(partial_b))
    if partial_a[:min_len] != partial_b[:min_len]:
        return False

    if len(seq_ints) + 1 < max_seq_len:
        return any(seq_exists(seq_ints + [i], partial_a + seq_a[i], partial_b + seq_b[i]) for i in range(seq_len))

if not seq_exists():
    print("No solution.")
