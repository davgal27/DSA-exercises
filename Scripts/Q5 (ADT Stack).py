# Write a program that uses an ADT Stack to evaluate arithmetic expressions in RPN
# format. The contents of the stack should be displayed on the screen during
# evaluation. The allowed arithmetic operators are +, -, x, and /.

def evaluate_rpn(expr):
    stack = []

    for item in expr.split():
        if item.isdigit(): #If the item from the split is a number
            stack.append(float(item)) # Add the item to the stack
        else: #If the item is not a number (operand)
            b = stack.pop() # Popping in LIFO format
            a = stack.pop()
            print(f"Operation: {a} {item} {b}")
            if item == '+':
                result = a + b
            elif item == '-':
                result = a - b
            elif item == 'x':
                result = a * b
            elif item == '/':
                result = a / b
            result  = round(result, 2)
            stack.append(result)
        print("Stack:", stack)
    return stack[0]

evaluate_rpn("4 6 + 2 x 3 / 8 - 10 +")

