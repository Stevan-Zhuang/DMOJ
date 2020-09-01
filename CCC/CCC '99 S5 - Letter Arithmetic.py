from itertools import permutations

def get_solution(map={}, idx=-1, carry=0):
    if idx >= 0:
        try: top = map[r_word1[idx]]
        except: top = 0
        try: middle = map[r_word2[idx]]
        except: middle = 0
        bottom = map[r_word3[idx]]

        result = (top + middle + carry) % 10
        carry = (top + middle + carry) // 10
        if result != bottom:
            return False

        if idx == len(word3) - 1:
            if not any(map[word[0]] == 0 for word in (word1, word2, word3)) and carry == 0:
                for word in (word1, word2, word3):
                    print("".join(str(map[letter]) for letter in word))
                return True
            return False

    idx += 1
    unique_letters = set(r_word1[idx: idx + 1] + r_word2[idx: idx + 1] + r_word3[idx: idx + 1]) - set(map.keys())
    unused_digits = set(range(10)) ^ set(map.values())
    return any(get_solution({**map, **{letter: digit for letter, digit in zip(unique_letters, digits)}},
                            idx, carry)
               for digits in permutations(unused_digits, len(unique_letters)))

for case in range(int(input())):
    word1, word2, word3 = input(), input(), input()
    r_word1, r_word2, r_word3 = word1[::-1], word2[::-1], word3[::-1]
    get_solution()
