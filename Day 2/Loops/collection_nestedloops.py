## This code demonstrates nested loops to print list of lists
# It iterates through a list of lists and prints each element in a formatted way

ll= [[10,20,30],[40,50,60],[70,80,90]]
for i in ll:
    for j in i:
        print(j, end=' ')
    print()  # Print a new line after each inner loop completes