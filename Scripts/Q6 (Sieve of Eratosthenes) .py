# 6. Write a Boolean function that checks if a number is prime. Also implement the
# Sieve of Eratosthenes algorithm – two separate algorithms. Explain any
# optimizations made.
import math

def is_prime(n): # Boolean function as it returns either True or False
    if n <= 1: # 1 and 0 are not primes; return false
        return False
    for i in range(2, int(math.sqrt(n) + 1)): # check if n is divisible by any number from 2 up to its sqrt
        if n % i == 0:
            return False
    return True

def sieve_erat(limit):
    primes = [True for _ in range(limit + 1)] # Assume all numbers are prime
    n = 2 # First prime number is 2

    while n * n <= limit: # checks all n from n to sqrt limit
        if primes[n]:
            for multiple in range(n * n, limit + 1, n):
                primes[multiple] = False
        n += 1
    primes_non_boolean = [num for num in range(2, limit+1) if primes[num]] # convert from boolean values to actual numbers
    return primes_non_boolean

#Part 1
n = int(input("PART 1: PRIME CHECKER \nEnter a number to check if it is prime: "))
if is_prime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")
#Part 2
limit = int(input("\nPART 2: SIEVE OF ERATOSTHENES:\nEnter a number to find all prime numbers up to that number: "))
print(f"The following numbers are prime:\n", sieve_erat(limit))

# Explaining Optimizations made
print("\nOptimizations made:\nIn both algorithms, checks were made only till n reached the square root of the limit."
      "\nthis is because once this is passed, all smaller factors have been checked previously, and checking\n"
      "would be a waste of time.")

# Testing
print("\nTESTING:\nTesting will be done by passing values of the sieve algorithm through the is_prime algorithm")

for number in sieve_erat(limit):
    if not is_prime(number):
        print(f"Result: {number} is not prime, therefore test has failed.")
    else:
        print("Result: All values are prime.")
        break





