# Print decimal to binary in Python
# This code demonstrates how to convert a decimal number to binary

s=input("Enter a decimal number: ")
def decimal_to_binary(n):
    result =bin(n)
    return result[2:]  # Convert to binary and remove the '0b' prefix
print(decimal_to_binary(int(s)))  # Convert input to integer and print binary representation