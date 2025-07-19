# Global Variables in python
# Global variables are accessible throughout the entire program

def function():
    x=10
    global()['x']=20
    print(x)  # This will print the local variable x, which is 10

x=15
fun()
print(x)  # This will print the global variable x, which is 15