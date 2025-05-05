# Create two integer arrays A and B. The two arrays must contain at least 256
# elements but must be of unequal size. Populate both arrays with randomly
# generated integers between 0 and 1024. Sort array A using Shell Sort and array B
# using Quick Sort.
import random
# Creating Arrays A and B
A: list[int] = [random.randint(0, 1024) for _ in range(500)]
B = [random.randint(0, 1024) for _ in range(300)]

# Sorting array A with Shell Sort
def shell_sort(A):
    n = len(A)
    gap = n // 2

    while gap > 0: # While gap is larger than zero
        for i in range(gap, n): # iterate through elements 'gap' positions apart until the end
            temp = A[i]
            j = i

            while j >= gap and A[j - gap] > temp: # While element 'gap' positions away is greater than current value shift forward
                A[j] = A[j - gap]
                j -= gap # Check for earlier elements at gap positions

            A[j] = temp
        gap = gap // 2
    return A

# Sorting array B with Quick Sort
# Partitioning
def partition(B, left, right):
    pivot = B[right] # Setting pivot as rightmost element of list (randomized, so this is fair)
    pivot_pos = left - 1
    for j in range(left, right): # runs from left to right
        if B[j] <= pivot:
            pivot_pos = pivot_pos + 1
            (B[pivot_pos], B[j]) = (B[j], B[pivot_pos])
    (B[pivot_pos +1 ], B[right]) = (B[right], B[pivot_pos + 1]) # Placing pivot in correct position at the end of the loop
    return pivot_pos + 1

# Calling Quicksort recursively
def quick_sort(B, left, right):
    if left < right:
        pivot_index = partition(B, left, right) # finding pivot index from partition
        quick_sort(B, left, pivot_index - 1) # Sorting elements less than pivot
        quick_sort(B, pivot_index + 1, right) #Sorting elements greater than pivot
    return B

shell_sort(A)
quick_sort(B, 0, len(B) - 1)

# function used to print the array into readable chunks
def print_array_in_chunks(array, chunk_size=30):
    for i in range(0, len(array), chunk_size):
        print(array[i:i + chunk_size])

print("Sorted Array A:")
print_array_in_chunks(A)
print("\nSorted Array B:")
print_array_in_chunks(B)

# TESTING
# Check if A is sorted
print("\nA is sorted", all(A[i] <= A[i + 1] for i in range(len(A) - 1))) #All function in python which gives true if all elements of given instruction are true
# Check if B is sorted
print("B is sorted:", all(B[i] <= B[i + 1] for i in range(len(B) - 1)))




