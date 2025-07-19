# Returning Multiple Values in Python
# This code demonstrates how to return multiple values from a function in Python.

def add_multiply(x,y):
    sum=x+y
    mul=x*y
    sub=x-y
    return sum, mul, sub  # Returning multiple values as a tuple

s,m,sb = add_multiply_subtract(10, 20)  # Unpacking the returned tuple
print(s)
print(m)
print(sb)