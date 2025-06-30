## This code demonstrates nested loops to print pairs of numbers
# It iterates through two ranges and prints each combination of the outer and inner loop variables

for i in range(1,3):
    j=1
    while j<3:
        print(i, j)
        j=j+1
    print("End of inner loop")
