def rbs(x,k,l,h):
    if(l<=h):
        m=(l+h)//2
        if(x[m]==k):
            return m
        elif(k<x[m]):
            return rbs(x,k,l,m-1)
        else:
            return rbs(x,k,m+1,h)
    else:
        return -1
n=int(input())
x=list(map(int,input().split()))
k=int(input())
x.sort()
l=0
h=n-1
a=rbs(x,k,l,h)
if(a==-1):
    print("element not found")
else:
    print("element found at ",a)


'''n=int(input())
x=list(map(int,input().split()))
k=int(input())
x.sort()
l=0
h=n-1
flag=0 # data not identified
while(l<=h):
    m=(l+h)//2
    if(x[m]==k):
        flag=1
        break
    elif(x[m]>k):
        h=m-1
    else:
        l=m+1
if(flag==1):
    print("element found at ",m)
else:
    print("element not found")'''
