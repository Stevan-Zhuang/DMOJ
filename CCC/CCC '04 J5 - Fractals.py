levels, width, x_coord = [int(s) for s in input().split()]

lines = [((0, 1), (width, 1), (0, 1))]

for level in range(levels):
    for line in range(len(lines)):
        line_coord1, line_coord2, orient = lines.pop(0)

        size = tuple((line_coord2[axis] - line_coord1[axis]) // 3 for axis in range(2))

        lines.append((tuple(line_coord1[axis] for axis in range(2)),
                      tuple(line_coord1[axis] + size[axis] for axis in range(2)),
                      orient))

        lines.append((tuple(line_coord2[axis] - size[axis] for axis in range(2)),
                      tuple(line_coord2[axis] for axis in range(2)),
                      orient))

        lines.append((tuple(line_coord1[axis] + size[axis] + size[abs(axis - 1)] * orient[axis] for axis in range(2)),
                      tuple(line_coord2[axis] - size[axis] + size[abs(axis - 1)] * orient[axis] for axis in range(2)),
                      orient))
                      
        lines.append((tuple(line_coord1[axis] + size[axis] for axis in range(2)),
                      tuple(line_coord1[axis] + size[axis] + size[abs(axis - 1)] * orient[axis] for axis in range(2)),
                     (-orient[1], orient[0])))

        lines.append((tuple(line_coord2[axis] - size[axis] for axis in range(2)),
                      tuple(line_coord2[axis] - size[axis] + size[abs(axis - 1)] * orient[axis] for axis in range(2)),
                     (orient[1], orient[0])))

y_coords = []
for line in range(len(lines)):
    line_coord1, line_coord2, orient = lines.pop(0)
    if line_coord1[0] <= x_coord <= line_coord2[0]:
        for intersects in range(line_coord1[1], line_coord2[1] + 1):
            y_coords.append(intersects)

print(" ".join(str(coord) for coord in sorted(list(set(y_coords)))))
