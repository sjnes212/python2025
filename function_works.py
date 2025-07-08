# How function works

def first():
    print("First function called")
def second():
    print("Second function called") 
    first()
    print("Third function called")

print("Fourth function called")  # main code starts here 
second() # def second function is called 
print("Fifth function called") # main code ends here

# Output:
# Fourth function called
# Second function called
# First function called
# Third function called
# Fifth function called