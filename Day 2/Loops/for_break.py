#Using break statment in for loop 
# when condition met, it will exit the loop

n=int(input("Enter n: "))
for x in range(2, n+1):
    if n % x == 0:
        print(x)
        break  

    # If user enters 15 , n=15 , x=2 
    # 15/2 = 7.5 , not equal to 0
    # x=3 , 15/3 = 5 , condition met
    # print 3 and exit the loop
    
    