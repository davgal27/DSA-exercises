# Write a function that computes cosine or sine by taking the first n terms of the
# appropriate (Maclaurin?) series expansion. Be careful with computing large
# factorials.

import math

def cos(x, term_count): # Calculating Cosine
    while x > math.pi: # Keeping X in range of [-pi, pi]
        x -= 2 * math.pi
    while x < -math.pi:
        x += 2 * math.pi
    # FIRST TERM
    sign = 1
    numerator  = 1
    denominator = 1
    result_cos = sign * numerator / denominator
    # Rest of terms
    for n in range(1, term_count):
        numerator *= x * x
        denominator *=  (2 * n - 1) * (2 * n) # use previous denom in calculation
        sign  *= -1 # Alternating signs
        result_cos += sign * numerator / denominator
    return result_cos


def sin(x, term_count): # Calculating sine
    while x > math.pi:  # Keeping X in range of [-pi, pi]
        x -= 2 * math.pi
    while x < -math.pi:
        x += 2 * math.pi
    #FIRST TERM
    sign = 1
    numerator = x
    denominator = 1
    result_sin = sign * numerator / denominator
    # Rest of terms
    for n in range(1, term_count):
        numerator *= x * x
        denominator *= (2 * n + 1) * (2 * n)
        sign *= -1
        result_sin += sign * numerator / denominator
    return result_sin

print("Cos function calculation for first 5 terms and x = 5:", cos(50, 5))
print("Sin function calculation for first 5 terms and x = 5:", sin(50, 5))
# Testing
print("\nTesting: Comparing with in built functions of python:")
print("Cos:", math.cos(50))
print("Sin:", math.sin(50))