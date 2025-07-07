# Print LCM of two numbers without using GCD
# Least Common Multiple (LCM)   

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = max(a,b)
while(lcm > 0):
    # Check if lcm is divisible by both a and b
    if(lcm % a==0 and lcm % b==0):
        break       
    lcm= lcm + 1
print("LCM is:", lcm)