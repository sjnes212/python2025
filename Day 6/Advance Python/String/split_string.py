# Print split string in Python
# This code demonstrates how to split a string into a list of words

s1="Hello, how are you doing today?"
print(s1.split())  # Default split by whitespace
s2="apple,banana,cherry"
print(s2.split(","))  # Split by comma
l=["apple", "banana", "cherry"]
print(" ".join(l))  # Join list into a string with space as separator
print(", ".join(l))  # Join list into a string with comma and space as separator