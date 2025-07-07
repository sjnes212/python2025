#print the divisors of a number
# This code finds the divisors of a number by checking each number from 1 to n

n=int(input("Enter a number: "))
x=1
while x <= n:
    if n % x == 0:
        print(x, end=' ')
    x=x+1