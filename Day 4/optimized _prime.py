# This code checks if a number is prime or not
# Prints "Yes" if it is prime, otherwise "No".

n=int(input("Enter a number: "))
if n <= 0:
    print("No")
else:
    x=2
    while x * x <= n:
        if n % x == 0:
            print("No")
            break
        x=x+1
    else:
        print("Yes")