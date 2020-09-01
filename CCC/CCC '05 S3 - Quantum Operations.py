tensor_product = [[1]]
for operation in range(int(input())):
    prev_num_rows = len(tensor_product)
    prev_num_cols = len(tensor_product[0])

    num_rows, num_cols = [int(s) for s in input().split()]
    matrix = [[int(s) for s in input().split()] for row in range(num_rows)]

    product = [[0 for col in range(prev_num_cols * num_cols)] for row in range(prev_num_rows * num_rows)]
    for row in range(prev_num_rows):
        for col in range(prev_num_cols):
            for oth_row in range(num_rows):
                for oth_col in range(num_cols):
                    product[row * num_rows + oth_row][col * num_cols + oth_col] = tensor_product[row][col] * matrix[oth_row][oth_col]

    tensor_product = product

    prev_num_rows = num_rows
    prev_num_cols = num_cols
    
print(max(max(row) for row in tensor_product))
print(min(min(row) for row in tensor_product))

sum_rows = [sum(row) for row in tensor_product]
print(max(sum_rows))
print(min(sum_rows))

sum_cols =  [sum(tensor_product[row][col] for row in range(len(tensor_product))) for col in range(len(tensor_product[0]))]
print(max(sum_cols))
print(min(sum_cols))
