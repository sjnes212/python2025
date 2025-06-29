#Take input number from the user and check if the number is positive, negative or zero
# if positive print "Positive" if negative print "Negative" else print "Zero"
n = int(input("Enter a number:"))
if n>0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")