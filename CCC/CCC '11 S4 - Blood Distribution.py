blood_counts = [int(data) for data in input().split()]
patient_counts = [int(data) for data in input().split()]

can_revieve = [
    [0],
    [1, 0],
    [2, 0],
    [3, 2, 1, 0],
    [4, 0],
    [5, 4, 1, 0],
    [6, 4, 2, 0],
    [7, 6, 5, 4, 3, 2, 1, 0]
]

max_patients = 0
for idx1 in range(8):
    for idx2 in can_revieve[idx1]:
        can_give = min(blood_counts[idx2], patient_counts[idx1])
        max_patients += can_give
        patient_counts[idx1] -= can_give
        blood_counts[idx2] -= can_give
        
print(max_patients)
