def find_extreme_points(arr):
    extremes = []
    for i in range(1, len(arr) - 1):
        if (arr[i - 1] < arr[i] > arr[i + 1]) or (arr[i - 1] > arr[i] < arr[i + 1]):
            extremes.append(arr[i])
    return extremes if extremes else "SORTED"

# Comment: An array is not guaranteed to be sorted just because it has no extremes.
# Example: [1, 1, 1, 1] has no extremes but is constant, not sorted in increasing/decreasing order.
