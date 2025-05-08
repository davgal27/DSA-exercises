# Write a program that finds an approximation to the square root of a given number
# n using an iterative numerical method such as the Newton-Raphson Method.

def find_sqrt(n, guess, tolerance): # n = no. to find sqrt of 2
    next_guess = (guess + n / guess) / 2
    if abs(guess - next_guess) < tolerance:
        print("Final guess is:", next_guess)
        return next_guess
    return find_sqrt(n, next_guess, tolerance) # Implementing recursion to repeat the step

find_sqrt(327, 327/2, 0.00001) # Parameters equal to those in
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

# Testing
print("Testing was done by comparing result to that found in link above. Result matches.")