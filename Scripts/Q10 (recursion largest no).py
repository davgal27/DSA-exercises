def find_largest_recursive(arr, n=None):
    if n is None: n = len(arr)
    if n == 1:
        return arr[0]
    return max(arr[n-1], find_largest_recursive(arr, n-1))
