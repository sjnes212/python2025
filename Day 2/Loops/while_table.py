#print a table of any number enter by user using a while loop
# This code will print the multiplication table of a number entered by the user

n = int(input("Enter a number to print its table: "))
# Get the number of terms to print in the table
m = int(input("Enter the number user wants to print: ")) 

i = 1
# while i <= 10: # Loop from 1 to 10
while i <= m: # Loop used for user defined number of terms
    print(i*n)
    i = i + 1 