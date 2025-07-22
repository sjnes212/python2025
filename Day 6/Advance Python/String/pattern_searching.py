# Print pattern searching in Python
# This code demonstrates how to find a substring within a string

txt=input("Enter Text: ")
pattern=input("Enter Pattern: ")
position=txt.find(pattern)  # Find the first occurrence of the pattern
while position >=0:
    print(position)  # Print the position of the found pattern
    position=txt.find(pattern, position + 1)  # Find the next occurrence of the pattern