spreadsheet = [input().split() for _ in range(10)]

def get_value(row, col, path = []):
    cell = spreadsheet[row][col]
    if not any(s in "ABCDEFGHIJ" for s in cell):
        return cell

    value = 0
    for data in cell.split("+"):
        if data in path:
            value = -10000000001
            break
        value += int(get_value("ABCDEFGHIJ".index(data[0]), "123456789".index(data[1]), path + [data]))

    value = str(value)
    spreadsheet[row][col] = value
    return value

for row in range(10):
    for col in range(9):
        get_value(row, col)

for row in spreadsheet:
    print(" ".join("*" if int(cell) < 0 else cell for cell in row))
