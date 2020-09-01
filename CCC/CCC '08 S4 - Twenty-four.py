from itertools import permutations

def add(n1, n2):      return n1 + n2
def subtract(n1, n2): return n1 - n2
def multiply(n1, n2): return n1 * n2
def divide(n1, n2):   return n1 // n2

invalid = -1
def operate(n1, n2, operation):
    if n1 <= invalid or n2 <= invalid: return invalid
    if operation == divide and (n2 == 0 or (n1 / n2) % 1 != 0): return invalid
    return operation(n1, n2)

def eval(cards, operations):
    result = cards[0]
    for i in range(3):
        result = operate(result, cards[i + 1], operations[i])
    return result

def eval_special(cards, operations):
    op1, op2, op3 = operations
    return operate(operate(cards[0], cards[1], op1), operate(cards[2], cards[3], op3), op2)

for case in range(int(input())):
    cards = [int(input()) for card in range(4)]
    operations = [add, subtract, multiply, divide]

    best_24 = 0
    for op1 in operations:
        for op2 in operations:
            for op3 in operations:
                for perm_cards in permutations(cards, 4):
                    result = eval(perm_cards, [op1, op2, op3])
                    if result > best_24 and result <= 24:
                        best_24 = result
                    result = eval_special(perm_cards, [op1, op2, op3])
                    if result > best_24 and result <= 24:
                        best_24 = result
    print(best_24)
