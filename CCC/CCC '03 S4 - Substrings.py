def suffix_array(string):
    char_order = sorted((string[idx:], idx) for idx in range(len_str))
    return [idx for _, idx in char_order]

def kasai(string, suffix_arr):
    longest_prefix = [0] * len_str
    suffix_inverse = [0] * len_str
    for idx in range(len_str):
        suffix_inverse[suffix_arr[idx]] = idx

    largest = 0
    for idx in range(len_str):
        if suffix_inverse[idx] == len_str - 1:
            largest = 0
            continue

        next_idx = suffix_arr[suffix_inverse[idx] + 1]
        while ( idx + largest < len_str and next_idx + largest < len_str
                and string[idx + largest] == string[next_idx + largest]):
            largest += 1

        longest_prefix[suffix_inverse[idx]] = largest
        if largest > 0:
            largest -= 1

    return longest_prefix

n_cases = int(input())
for case in range(n_cases):
    string = input()
    len_str = len(string)

    suffix = suffix_array(string)
    lcp = kasai(string, suffix)

    result = len_str - suffix[0] + 1
    for idx in range(1, len(lcp)):
        result += (len_str - suffix[idx]) - lcp[idx - 1]; 

    print(result)
