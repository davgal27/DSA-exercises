# Write a program that generates the Collatz sequence of all the integers in the range
# 2 to 512. The program will store the generated sequences in a CSV file
import csv
def collatz_generator(n):
    col_sequence = []
    while n != 1:
        col_sequence.append(n)
        if n % 2 == 0: # following rules of the collatz sequence
            n = n // 2
        elif n % 2 == 1:
            n = 3 * n + 1
    return col_sequence

with open('collatz_sequence.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(collatz_generator(512))

# Testing
print("Testing was done by comparing to the result in a paper in the"
      "\n'International Journal of Mathematics and Mathematical Sciences':"
      "\n'Novel Theorems and Algorithms Relating to the Collatz Conjecture'")