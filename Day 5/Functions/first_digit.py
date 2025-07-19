# Print the First Digit of a Number

def getFirstDigit(x):
    while x >= 10:
        x //= 10  # Reduce x by removing the last digit
    return x  # Return the first digit  

x=int(input("Enter a number: "))
print(getFirstDigit(x))  # Call the function and print the first digit
