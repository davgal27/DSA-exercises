def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def cosine(x, n_terms):
    result = 0
    for n in range(n_terms):
        result += ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
    return result

def sine(x, n_terms):
    result = 0
    for n in range(n_terms):
        result += ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
    return result
