for case in range(int(input())):
    expression = input().split()
    operations = [[expression[idx], idx] for idx in range(len(expression))
                  if expression[idx] in 'X+-']
    operations.sort(key=lambda x: x[0] == 'X', reverse=True)

    for idx1 in range(len(operations) - 1):
        op, op_idx = operations[idx1]

        expression[op_idx] = "({} {} {})".format(expression[op_idx - 1], op, expression[op_idx + 1])
        expression.pop(op_idx + 1)
        expression.pop(op_idx - 1)

        for idx2 in range(len(operations)):
            if operations[idx2][1] > op_idx:
                operations[idx2][1] -= 2

    print(" ".join(expression))
