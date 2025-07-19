# This code demonstrates the use of variable length arguments in a function.
# Keyword variable length arguments

def printDetails(id, **details):
    print(f"Details for ID {id}:")
    for d,v in details.items():
        print(f"{d} : {v}")

printDetails(101, name="abc", price=200)
print()
printDetails(102, name="xyz",color="black")
