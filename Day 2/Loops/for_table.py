#print a table of any number enter by user using a for loop
n = int(input("Enter a number to print its table: "))
# Get the number of terms to print in the table
m= int(input("Enter the number user wants to print: "))

# for i in range(1, 11):  # Loop from 1 to 10
for i in range(1, m+1):  # Loop from 1 to 10
    print(i * n)  # Print the product of i and n

