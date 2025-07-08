# Print the sum of elements using def functions

def sum(init_sum, *elements):
    total = init_sum
    for x in elements:
        total= total+x  
    return total
print(sum(0,10,20))
print(sum(5,10,15))