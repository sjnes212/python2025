#Print multiple of 3 when user enter the number using while break
n=int(input("Enter number:"))
x=2
while x <= n:
    if n % x == 0:
        print(x)
        break  # Exit the loop when a multiple of n is found
    x =x+1

