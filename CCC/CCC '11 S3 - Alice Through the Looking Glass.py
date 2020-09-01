crystal = [[0, 1, 1, 1, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

def magnify(x, y, depth=1):
    magnification = 5 ** (max_depth - depth)
    x_zoom = x // magnification
    y_zoom = y // magnification

    if crystal[y_zoom][x_zoom] == 1:
        return "crystal"
    if crystal[y_zoom][x_zoom] == 0:
        if depth >= max_depth or (y_zoom - 1 < 0 or crystal[y_zoom - 1][x_zoom] == 0):
            return "empty"
        return magnify(x % magnification, y % magnification, depth + 1)
    
num_cases = int(input())
for case in range(num_cases):
    max_depth, x, y = [int(data) for data in input().split()]
    print(magnify(x, y))
    
