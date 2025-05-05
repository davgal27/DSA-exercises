def evaluate_rpn(expr):
    stack = []
    tokens = expr.split()
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            if token == '+': result = a + b
            elif token == '-': result = a - b
            elif token == 'x': result = a * b
            elif token == '/': result = a / b
            stack.append(result)
        print("Stack:", stack)
    return stack[0]

# Example usage
# evaluate_rpn("3 4 + 2 x 7 /")
