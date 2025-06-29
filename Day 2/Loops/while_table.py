#print a table of any number enter by user using a while loop
n = int(input("Enter a number to print its table: "))
# Get the number of terms to print in the table
m = int(input("Enter the number user wants to print: ")) 

i = 1
# while i <= 10:
while i <= m:
    print(i*n)
    i = i + 1 