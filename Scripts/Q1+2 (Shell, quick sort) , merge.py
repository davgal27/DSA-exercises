# Create two integer arrays A and B. The two arrays must contain at least 256
# elements but must be of unequal size. Populate both arrays with randomly
# generated integers between 0 and 1024. Sort array A using Shell Sort and array B
# using Quick Sort.
import random
# Creating Arrays A and B
A = [random.randint(0, 1024) for _ in range(500)]
B = [random.randint(0, 1024) for _ in range(300)]

# Sorting array A with Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0: # While gap is larger than zero
        for i in range(gap, n): # iterate through elements 'gap' positions apart until the end
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp: # While element 'gap' positions away is greater than current value shift forward
                arr[j] = arr[j - gap]
                j -= gap # Check for earlier elements at gap positions

            arr[j] = temp
        gap = gap // 2
    return arr

# Sorting array B with Quick Sort
# Partitioning
def partition(arr, left, right):
    pivot = arr[right] # Setting pivot as rightmost element of list (randomized, so this is fair)
    pivot_pos = left - 1
    for j in range(left, right): # runs from left to right
        if arr[j] <= pivot:
            pivot_pos = pivot_pos + 1
            (arr[pivot_pos], arr[j]) = (arr[j], arr[pivot_pos])
    (arr[pivot_pos +1 ], arr[right]) = (arr[right], arr[pivot_pos + 1]) # Placing pivot in correct position at the end of the loop
    return pivot_pos + 1

# Calling Quicksort recursively
def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right) # finding pivot index from partition
        quick_sort(arr, left, pivot_index - 1) # Sorting elements less than pivot
        quick_sort(arr, pivot_index + 1, right) #Sorting elements greater than pivot
    return arr

shell_sort(A)
quick_sort(B, 0, len(B) - 1)

# function used to print the array into readable chunks
def print_array_in_chunks(arr, chunk_size=30):
    for i in range(0, len(arr), chunk_size):
        print(arr[i:i + chunk_size])

print("QUESTION 1: \nSorted Array A of size:", len(A))
print_array_in_chunks(A)
print("\nSorted Array B of size:", len(B))
print_array_in_chunks(B)

# TESTING
# Check if A is sorted
print("\nA is sorted", all(A[i] <= A[i + 1] for i in range(len(A) - 1))) #All function in python which gives true if all elements of given iterable are true
# Check if B is sorted
print("B is sorted:", all(B[i] <= B[i + 1] for i in range(len(B) - 1)))

########### QUESTION 2
# Take the two sorted arrays A and B from Question 1 above and merge into a new
# array C. You must do this in linear time. Note that the size of C must be size of A
# plus size of B. Use the merging technique used in Merge Sort.

def merge_arrays(arr1, arr2):
    i = 0 # For A
    j = 0 # For B
    k = 0 # For C
    n = len(arr1)
    m = len(arr2)
    joined_arr = [k] * (n + m)  # Create array joined size of A + B

    while i < n and j < m: # While both indexes are in bounds of their respective arrays:
        if arr1[i] <= arr2[j]: # Compare elements from both arrays and add smaller one to C
            joined_arr[k] = arr1[i] # smaller goes to A
            i = i + 1
        else:
            joined_arr[k] = arr2[j] # smaller goes to B
            j = j + 1
        k = k + 1 # increment index k of C by one after each comparison

    while i < n: # If any elements left over in A (in case A is larger than B) move element to C
        joined_arr[k] = arr1[i]
        i = i + 1
        k = k + 1

    while j < m: # Same thing for B
        joined_arr[k] = arr2[j]
        j = j + 1
        k = k + 1
    return joined_arr

C = merge_arrays(shell_sort(A), quick_sort(B, 0, len(B) - 1))
print("\n\nQUESTION 2: \nSorted Array C of size:", len(C))
print_array_in_chunks(C)
print("\n C is sorted:", all(C[i] <= C[i + 1] for i in range(len(C) -1)))