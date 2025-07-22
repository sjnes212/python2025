# Print binary to decimal in Python
# This code demonstrates how to convert a binary number to decimal

s=input("Enter a binary number: ")
# Alternative method using built-in function
def binary_to_decimal(b):
    result=int(b, 2)  # Convert binary string to decimal using base 2
    return result
print(binary_to_decimal(s))  # Convert input to decimal and print result