sheeps = [(float(input()), float(input())) for sheep in range(int(input()))]
for sheep in set(sorted(((sheep[0] - point) ** 2 + sheep[1] ** 2, sheep) for sheep in sheeps)[0][1] for point in (x * 0.05 for x in range(20001))):
    print("The sheep at ({:.2f}, {:.2f}) might be eaten.".format(sheep[0], sheep[1]))
