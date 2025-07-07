# Print lcm using GCD algorithm
# Least Common Multiple (LCM) using GCD

import math
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
gcd = math.gcd(a, b)
lcm = (a * b) // gcd    
print("LCM is:", lcm)