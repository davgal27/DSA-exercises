from collections import defaultdict

def find_2pairs_same_product(arr):
    product_map = defaultdict(list)
    n = len(arr)
    pairs = []

    for i in range(n):
        for j in range(i + 1, n):
            prod = arr[i] * arr[j]
            product_map[prod].append((arr[i], arr[j]))

    for prod, pair_list in product_map.items():
        if len(pair_list) > 1:
            for i in range(len(pair_list)):
                for j in range(i + 1, len(pair_list)):
                    a, b = pair_list[i]
                    c, d = pair_list[j]
                    if len({a, b, c, d}) == 4:
                        pairs.append(((a, b), (c, d)))
    return pairs

sample_list = [random.randint(1, 1024) for _ in range(100)]
pairs_with_same_product = find_2pairs_same_product(sample_list)
