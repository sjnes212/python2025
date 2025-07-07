# Print the number of digits in a number
# Example: Input: 12345 Output: 5

x= int(input("Enter a number: "))
count = 0
while x > 0:
    x = x // 10
    count = count + 1
print("Number of digits in the number is:", count)