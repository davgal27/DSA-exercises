import csv

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

with open('collatz_sequences.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(2, 513):
        writer.writerow([i] + collatz_sequence(i))
