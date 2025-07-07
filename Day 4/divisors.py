# this code finds the divisors of a number .

n=int(input("Enter a number: "))
for x in range(1, n + 1):
    if n % x == 0:
        print(x, end=' ')