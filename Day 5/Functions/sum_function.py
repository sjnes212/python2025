# Print the sum of elements using def functions

def sum(*elements):
    total = 0
    for x in elements:
        total= total + x
    return total
print(sum(10,20))
print(sum(10,20,30))
print(sum(10))
print(sum())
