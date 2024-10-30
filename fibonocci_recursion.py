'''def fib(n):
    if(n==1):
        return 1
    if(n==0):
        return 0
    else:
        return(fib(n-1)+fib(n-2))
n=int(input())
if n<=0:
    print("invalid input")
else:
    for i in range(n):
        x=fib(i) #calling function
        print(x,end=' ') '''

n=int(input())
a=[0,1]
if(n==1):
    print(a[0])
elif(n==2):
    print(a)
else:
    for i in range(2,n):
        x=a[i-1]+a[i-2]
        a.append(x)
    print(a)


