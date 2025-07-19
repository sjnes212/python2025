# Print first digit of a number using math module

import math
def getFirstDigit(x):
    d=int(math.log10(x))  # Get the number of digits in x
    res=x // (10 ** d)  # Get the first digit
    return res  # Return the first digit

x=int(input("Enter a number: "))
print(getFirstDigit(7549))  # Call the function and print the first digit