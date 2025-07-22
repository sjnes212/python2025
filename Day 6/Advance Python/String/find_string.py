# Print find string in Python
# This code demonstrates how to find a substring within a string

s1="Hi there, how are you?"
s2="how"
print(s1.find(s2))  # Returns the index of the first occurrence of 's2' in 's1'
print(s1.index(s2))  # Similar to find, but raises an error if 's2' is not found
print(s1.count(s2))  # Counts how many times 's2' appears in 's1'
print(s1.find("hello"))
n=len(s1)  # Length of the string 's1'
print(s1.find(s2,1,n))  # Find 's2' starting from index 1 to n