# This program calculates the Fibonacci sequence up to a given number by user input.
# example: n=5
# Output: 0 1 1 2 3 5

n = int(input("Enter a number: "))
a=0
b=1
print("Fibonacci sequence upto", n, "is:")
while a <= n:
    print(a, end=' ')
    (a, b) = (b, a + b)  # Update a and b to the next two numbers in the sequence   
print()  # Print a newline at the end