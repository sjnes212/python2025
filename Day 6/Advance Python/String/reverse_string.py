# Print reverse string in Python
# This code demonstrates how to reverse a string in Python

s=input("Enter a string to reverse: ")
reverse=""
for i in s:  # Iterate through each character in the string
    reverse=i+reverse  # Prepend each character to the reverse string
print(reverse)  # Print the reversed string

print(s[::-1])  # Alternative method using slicing to reverse the string