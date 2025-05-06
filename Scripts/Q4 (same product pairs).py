# Write a program that, given a list of integers, finds all 2-pairs of integers that have
# the same product. A 2-pair is 2 distinct pairs of integers ((a,b),(c,d)) where a X b = c
# X d and a ≠ b ≠ c ≠ d. The range of integers in the list should be from 1 to 1024.
import random
from collections import defaultdict

random_array = [random.randint(1, 1024) for _ in range(50)]

def find_pairs_same_product(arr):
    pairs_same_product = []
    product_map = defaultdict(list)
    seen_combinations = []

    for i in range(len(arr)): # Iterating over all pairs of i and j
        for j in range(i + 1, len(arr)):
            a = arr[i]
            b = arr[j]
            product = a * b

            for (c,d) in product_map[product]: # If any pair has the same product
                group = {a, b, c, d} # Creating a set to be checked for length, if 4, all unique
                if len({a, b, c, d}) == 4: # If length is 4, all are unique due to nature of set

                    if group not in seen_combinations:
                        pairs_same_product.append(((a, b), (c, d), product))
                        seen_combinations.append(group) # Mark as seen to avoid duplicates

            product_map[product].append((a, b)) # Add pair only if another pair has same product

    return pairs_same_product

def print_results(arr): # Function for printing a fail case with no pairs found
    pairs = find_pairs_same_product(arr)
    if pairs:
        for pair1, pair2, product in pairs:
            print(f"pair 1:{pair1}, pair 2:{pair2}. Product is: {product}")
    else:
        print("No matching pairs found.")
print("Results for random array:")
print_results(random_array)

# TESTING: Done with two different arrays: one known to have no matching products, and one with known matching products
matching_array = [2, 16, 1, 32, 8, 4]
nomatching_array = [1, 2, 3, 5, 7]
print("\nTESTING: Results with a matched array:")
print_results(matching_array)

print("\nTESTING: Results with an array known to have no matches. Expected result is no matches found:")
print_results(nomatching_array)



