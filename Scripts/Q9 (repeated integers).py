from collections import Counter

def find_duplicates(arr):
    count = Counter(arr)
    return [num for num, freq in count.items() if freq > 1]
