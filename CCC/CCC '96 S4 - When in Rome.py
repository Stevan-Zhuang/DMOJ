numeral_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
for case in range(int(input())):
    expression = input()
    numerals = expression.replace("+", " ").replace("=", " ").split()

    value = 0
    for num in numerals:
        for idx in range(len(num)):
            if (   (idx + 3 < len(num) and
                    all(num[idx + shift_idx] == num[idx + shift_idx + 1]
                        for shift_idx in range(len(num) - 1))) or 
                   (idx + 1 < len(num) and
                    numeral_values[num[idx + 1]] > numeral_values[num[idx]])):
                value -= numeral_values[num[idx]]
                continue
            value += numeral_values[num[idx]]

    if value > 1000:
        print(expression + "CONCORDIA CUM VERITATE")
        continue

    fives = ['V', 'L', 'D', '']
    ones = ['I', 'X', 'C', 'M']
    digits = str(value)
    result = ""

    for idx in range(len(digits)):
        digit = int(digits[idx])
        idx = len(digits) - 1 - idx

        if digit <= 3:   result += ones[idx] * digit
        elif digit <= 5: result += ones[idx] * (5 - digit) + fives[idx]
        elif digit <= 8: result += fives[idx] + ones[idx] * (digit - 5)
        else:            result += ones[idx] * (10 - digit) + ones[idx + 1]

    print(expression + result)
