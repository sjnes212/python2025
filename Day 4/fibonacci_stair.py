# Print Fibonacci sequence of stair numbers up to a given number by user input.
# example: n=5
# Output: 1 1 2 3 5 8

n=int(input("Enter a number: "))
if n==0:
    print(1)
elif n==1:
    print(1,1)
else:
    print(1,1, end=' ')
    a=1
    b=1
    for i in range(2, n+1):
        c=a+b
        print(c, end=' ')
        a=b
        b=c