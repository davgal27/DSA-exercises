# Write a function that returns the sum of the first n numbers of the Fibonacci sequence

def first_n_fibonacci_numbers(n):
    sequence = []
    x = 0 # Starting values of x and y of the sequence
    y = 1
    for i in range(n):
        sequence.append(x)
        temp = x # use temp for old x as x will be updated in next step, and thus affect y
        x = y
        y = temp + y
    return sequence

print(first_n_fibonacci_numbers(20))

# Testing
# Below is the first 20 numbers of the fibonacci sequence
# pasted from wikipedia. It will be used to compare the function's output
fibonacci_wikipedia = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
print(f"wikipedia array is:\n", fibonacci_wikipedia)


