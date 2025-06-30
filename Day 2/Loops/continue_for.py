# Print all number in a list that are not multiples of 5
# This code demonstrates the use of a continue statement in a loop.

l = [10,16, 17, 18, 19, 15]
for x in l:
    if x % 5 == 0:  # Check if the number is a multiple of 5
    # if x % 5 !=0: # Check if the number is not a multiple of 5 , no require # to use this continue statement  

        continue 
    print(x)  # Print the number if it is not a multiple of 5

# Output:
# 16        
# 17
# 18
# 19
# 10 is skipped because it is a multiple of 5
# 15 is skipped because it is a multiple of 5
