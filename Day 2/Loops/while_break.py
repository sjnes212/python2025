#Using break statment in while loop 
# when condition met, it will exit the loop

n=int(input("Enter number:"))
x=2
while x <= n:
    if n % x == 0:
        print(x)
        break  
    x =x+1

# If user enters 15 , n=15 , x=2 
    # 15/2 = 7.5 , not equal to 0
    # x=2+1=3
    # x=3 , 15/3 = 5 , condition met
    # print 3 
    # break exit the loop