n=int(input("Enter n: "))
for x in range(2, n+1):
    if n % x == 0:
        print(x)
        break  # Exit the loop when a multiple of 3 
    