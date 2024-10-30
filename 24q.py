n=int(input())#10
m=int(input())#3
x=n-m
if(m==0):
    print("Invalid input")
    print("candies available : ",n)
elif(x>=5):
    print("candies sold : ",m)
    print("Candies available : ",x)
else:
    print("Invalid input")
    

