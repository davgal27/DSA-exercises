# Write a program that, given an array of integers, finds all integers in the array that
# are repeated more than once. Try to find a fast and memory-efficient way of doing this

arr_has_repeats = [1, 7, 7, 2, 3, 4, 4, 5, 6, 1, 55, 0, 0, 32, 3] # Repeated values: 4, 7, 1, 0, 3
arr_no_repeats = [34, 15, 28, 2, 3, 44, 4]
# Try 1 (unsuccessful: although this performs the task, time complexity is O(n^2))
def find_repeats_try1(arr):
    repeats =  []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (i != j # if not comparing with itself
            and arr[i] == arr[j]  # and value at 1 position is the same as that at another
            and arr[i] not in repeats): # and has not already been listed as a repeat
                repeats.append(arr[i]) # add it to the repeats array
    return repeats if repeats else "NO REPEATS FOUND"


# Try 2 (successful: O(n) time complexity)
def find_repeats(arr):
    seen = set()
    repeats = set()
    for number in arr:
        if number not in seen:
            seen.add(number)
        else:
            repeats.add(number)
    return repeats if repeats else "NO REPEATS FOUND"

print(f"Duplicates in the array known to have repeats:", find_repeats(arr_has_repeats))
# Testing
print(f"An array known to have no duplicates was used to test the program:\n", find_repeats(arr_no_repeats))

