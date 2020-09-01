data = [int(data) for data in input().split()]
tele_start, tele_end = [(data[0], data[1]), (data[2], data[3])]

def get_orientation(point1, point2, point3):
    slope1 = (point2[1] - point1[1]) * (point3[0] - point2[0])
    slope2 = (point3[1] - point2[1]) * (point2[0] - point1[0])

    if slope1 > slope2:
        return "clockwise"
    if slope1 < slope2:
        return "counterclockwise"
    return "colinear"

def on_segment(point1, point2, point3):
    return (point3[0] <= max(point1[0], point2[0]) and point3[0] >= min(point1[0], point2[0]) and 
            point3[1] <= max(point1[1], point2[1]) and point3[1] >= min(point1[1], point2[1]))

count = 0
for building in range(int(input())):
    data = [int(data) for data in input().split()]
    line_points = [(data[i], data[i + 1]) for i in range(1, data[0] * 2, 2)]

    for point in range(data[0] - 1, -1, -1):
        line_start = line_points[point]
        line_end = line_points[point - 1]

        cases = [(tele_start, tele_end, line_start),
                 (tele_start, tele_end, line_end),
                 (line_start, line_end, tele_start),
                 (line_start, line_end, tele_end)]
        orients = [get_orientation(*cases[case]) for case in range(4)]

        if orients[0] != orients[1] and orients[2] != orients[3]:
            count += 1
            break
        if any(orients[case] == "colinear" and on_segment(*cases[case])
               for case in range(4)):
            count += 1
            break

print(count)
