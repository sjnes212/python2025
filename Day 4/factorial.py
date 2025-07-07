# This program calculates the factorial of a given number by user and how many ways you can arrange the number.

n=int(input("Enter a number: "))
factorial = 1
for i in range(2, n + 1):
    factorial = factorial * i; # This is equivalent to factorial = factorial * x

print("Factorial of", i, "is:", factorial)