num_cells, num_epochs = [int(data) for data in input().split()]
cells = [int(data) for data in input()]
new_cells = [0] * num_cells

binary = bin(num_epochs)[2:]
num_bits = len(binary)
for bin_idx, bin_r_idx in zip(range(num_bits), reversed(range(num_bits))):
    if binary[bin_idx] == '1':
        shift = 2 ** bin_r_idx
        for idx in range(num_cells):
            new_cells[idx] = (cells[(idx - shift) % num_cells] ^
                              cells[(idx + shift) % num_cells])
        cells = new_cells.copy()

print("".join(str(data) for data in new_cells))
