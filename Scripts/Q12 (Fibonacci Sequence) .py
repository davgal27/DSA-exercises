def fibonacci_sum(n):
    a, b = 1, 1
    total = a + b
    for _ in range(n - 2):
        a, b = b, a + b
        total += b
    return total

# Time: O(n)
