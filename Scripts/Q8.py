def sqrt_newton(n, tolerance=1e-10):
    guess = n
    while True:
        new_guess = (guess + n / guess) / 2
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess
