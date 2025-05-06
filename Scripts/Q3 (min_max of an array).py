# Let A be an array of n elements (that is, the elements of A are A[0], . . . , A[n−1]). An
# element A[i] is called extreme if the following conditions hold regarding A[i].
# • A[i] is not the first nor the last element of A. That is, 0 < i < n – 1 and either A[i
# − 1] < A[i] > A[i + 1] or A[i − 1] > A[i] < A[i + 1]. For example, the extreme
# points of an array [0, 5, 3, 6, 8, 7, 15, 9] are 5, 3, 8, 7, 15.
# Write an algorithm that prints the extreme points of the given array. If there are no
# extreme points, the algorithm prints “SORTED”. Do you agree that an array has no
# extreme points if and only if it is sorted? Explain your answer.

import random
A = [random.randint(0, 1024) for _ in range(10)]  # Short array for quick testing
B = [1, 2, 3, 4, 5, 6, 7, 10, 11, 55] # Example of sorted array for testing
def find_extremes(arr):
    extremes =  []
    for i in range(1, len(arr) - 1): # A[i] is not the first nor the last element of A
        if (arr[i - 1] < arr[i] > arr[i + 1]) or (arr[i - 1] > arr[i] < arr[i + 1]): # Check if i is larger or smaller than both neighbours
            extremes.append(arr[i]) # if it is, add it to the extremes array
    return extremes if extremes else "NONE, IT IS SORTED"

print("Array A Extremes:", find_extremes(A))

# TESTING
print("Array B Extremes:", find_extremes(B))  #This will always output sorted
# ANSWER TO QUESTION
print("I agree that an array has no extreme points if and only if it is sorted, as for an array to\n"
      "not have extreme points, it must be strictly ascending or descending; hence sorted")



