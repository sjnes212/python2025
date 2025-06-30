## This code demonstrates nested loops to print a multiplication table
# It iterates through numbers 1 to 10 and prints their multiples in a formatted way

for i in range(1, 11):
    for j in range(i, i*10+i,i):
        print(j, end=' ')
    print()  # Print a new line after each inner loop completes


