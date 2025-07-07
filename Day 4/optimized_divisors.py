# This code finds the divisors of a number in an optimized way by checking up to the square root of the number.
# It prints both the divisor and its corresponding quotient.

n=int(input("Enter a number: "))
x=1
while x * x < n:
    if n % x == 0:
        print(x)
        print(n/x)
    x= x+1
if x * x == n:
    print(x)