# This code demonstrates the use of keyword variable length arguments in a function.
# Keyword Variable Length Arguments

def printDetails(**details):
    for d,v in details.items():
        print(f"{d} : {v}")

printDetails(id=101,name="abc", price=100)
print()
printDetails(id=102,name="xyz")
