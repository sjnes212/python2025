# Print palindrome check in Python
# This code demonstrates how to check if a string is a palindrome

s=input("Enter a string to check for palindrome: ")
low=0
high=len(s)-1
while low < high:
    if s[low] != s[high]:
        print(f"{s} is not a palindrome")
        break
    low= low + 1
    high= high - 1
else:
    print(f"{s} is a palindrome")
# Alternative method using slicing
if s == s[::-1]:
    print(f"{s} is a palindrome (using slicing)")
else:
    print(f"{s} is not a palindrome (using slicing)")