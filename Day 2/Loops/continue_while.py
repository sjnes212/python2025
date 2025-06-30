# Print numbers from 0 to 5, skipping the number 3
# This code demonstrates the use of a continue statement in a while loop
# The continue statement skips the rest of the loop when a certain condition is met

i=0
while i<=5:
   if i == 3:
       i= i+1
       continue # Skip the rest of the loop when i is 3
   print(i, i*i)  # Print the value of i if it is not 3      
   i= i+1  # Increment i to avoid an infinite loop