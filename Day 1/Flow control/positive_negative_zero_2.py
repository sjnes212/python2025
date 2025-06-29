#Take input number from the user and check if the number is positive even, positive odd, negative even ,negative odd or zero
# if positive even print "Positive even" or "Positive odd" if negative print "Negative even" or "Negative odd" else print "Zero"
n = int(input("Enter a number:"))
if n>0:
    print("positive" ,end=' ')
    if n%2 == 0:
        print("even")
    else:
        print("odd")
    
elif n<0:
    print("negative", end=" ")
    if n%2 == 0:
        print("even")
    else:
        print("odd")
      
else:
    print("zero")