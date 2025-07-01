# Print the square pattern from the given user input
# This code will print a square pattern of asterisks based on the number of rows

n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()  # Move to the next line after printing one row