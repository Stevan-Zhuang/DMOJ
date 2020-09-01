input()
wood_lengths = [int(data) for data in input().split()]

max_wood_length = max(wood_lengths)
wood_length_counts = [0] * (max_wood_length + 1)
board_height_lengths = [0] * (max_wood_length * 2 + 1)

for wood_length in wood_lengths:
    wood_length_counts[wood_length] += 1

for wood_length1 in range(1, max_wood_length + 1):
    count1 = wood_length_counts[wood_length1]
    if count1 != 0:
        board_height_lengths[wood_length1 * 2] += count1 // 2
        for wood_length2 in range(1 + wood_length1, max_wood_length + 1):
            count2 = wood_length_counts[wood_length2]
            if count2 != 0:
                board_height_lengths[wood_length1 + wood_length2] += min(count1, count2)

max_fence_length = 0
count_heights = 0
for fence_length in board_height_lengths:
    if fence_length > max_fence_length:
        max_fence_length = fence_length
        count_heights = 0
    if fence_length == max_fence_length:
        count_heights += 1

print(max_fence_length, count_heights)
