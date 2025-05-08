# Write a recursive function that finds the largest number in a given list of integers.

def find_largest_number(arr, i = 0, highest = None):
    if i == len(arr): # Base Case: If reach the end of the list, return highest
        return highest
    if highest is None: # Case for the first run through (no highest set yet)
        highest = arr[i] # Set highest to the first number in array
    else:
        next_guess = arr[i] # Next guess will be current number in array
        if next_guess > highest: # if higher than previous number, new highest
            highest = next_guess
    return find_largest_number(arr, i+1, highest) # Recursive call

fifty_is_highest = [1, 49, 50, 22, 2, 33]
print("50 is the expected highest number. Program outputs:", find_largest_number(fifty_is_highest))

# Testing
print("\nThe program is tested by inputting and printing numerous arrays with known largest numbers")

test_arr1 = [1, 89, 23, 5, 465, 5]
print("465 is the expected largest number. Program outputs:", find_largest_number(test_arr1))
test_arr2 = [1, 89, 89, 89, 90]
print("90 is the expected largest number. Program outputs:", find_largest_number(test_arr2))
