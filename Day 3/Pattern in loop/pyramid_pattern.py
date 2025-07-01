# Print pyramid pattern where the number of rows is given by the user
# pyramid pattern is a common exercise in programming to understand loops and printing patterns.

n=int(input("Enter the number of rows: "))
for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")
    
    # Print stars
    for j in range(2 * i + 1):
        print("*", end="")
    
    # Move to the next line
    print()