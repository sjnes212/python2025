# Print list elements until a condition is met
# If a number is a multiple of 5, skip it; if it's a multiple of 7, break the loop
# Print the last value of x after the loop ends

l= [10,16,17,18,9,15,21,13]
for x in l:
    if x % 5 == 0:  # Check if the number is a multiple of 5
        continue  # Skip the rest of the loop when x is a multiple of 5
    if x%7 == 0:
       break
    print(x)  # Print the last value of x after the loop ends
print("Loop ended")  # Indicate that the loop has ended