from collections import Counter

needle = input()
haystack = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"
len_alphabet = len(alphabet)

prime_mod = 791661539476164852699949778849

def rabin_karp(needle, haystack):
    len_needle = len(needle)
    len_haystack = len(haystack)

    count_needle = Counter(needle + alphabet)
    count_haystack = Counter(haystack[:len_needle] + alphabet)

    for char in alphabet:
        count_needle[char] -= 1
        count_haystack[char] -= 1

    reverse = (len_alphabet ** (len_needle - 1)) % prime_mod

    hash_haystack = 0
    for idx in range(len_needle):
        hash_haystack = (len_alphabet * hash_haystack + ord(haystack[idx])) % prime_mod

    unique_hashes = set()

    for shift in range(len_haystack - len_needle + 1):
        if count_needle == count_haystack:
            unique_hashes.add(hash_haystack)

        if shift < len_haystack - len_needle:
            hash_haystack = (len_alphabet * (hash_haystack - ord(haystack[shift]) * reverse)
                             + ord(haystack[shift + len_needle])) % prime_mod
            count_haystack[haystack[shift]] -= 1
            count_haystack[haystack[shift + len_needle]] += 1

    return len(unique_hashes)

try:    print(rabin_karp(needle, haystack))
except: print(0)
