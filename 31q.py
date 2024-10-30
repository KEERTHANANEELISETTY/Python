def check(n):
    flag=0#third factor not identified.
    for i in range(2,(n//2)+1):
        if(n%i==0):
            flag=1#third factor identified for the number n.
            break
    if(flag==1 or n==0 or n==1):
        print("not prime")
    else:
        print("prime")
n=int(input())
if(n>=0):
    check(n)
else:
    print("please enter positive number")
    n=int(input())
    check(n)
