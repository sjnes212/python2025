# print strip in Python
# This code demonstrates how to strip characters from a string
# It only removes hypen(-) from the corners not from the middle

s="--Hello, W-o-r-l-d!--"
print(s.strip("-"))  # Remove leading and trailing dashes
print(s.lstrip("-"))  # Remove leading dashes   
print(s.rstrip("-"))  # Remove trailing dashes
print(s.strip("!-"))  # Remove leading and trailing dashes and exclamation marks