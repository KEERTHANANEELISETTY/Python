n=int(input())
x=list(map(int,input().split()))
x.sort()
k=int(input())
l=0
r=n-1
flag=0
while(l<=r):
    mid1=l+(r-l)//3
    mid2=r-(r-l)//3
    if(x[mid1]==k):
        flag=1
        pos=mid1
        break
    elif(x[mid2]==k):
        flag=1
        pos=mid2
        break
    elif(k<x[mid1]):
        r=mid1-1
    elif(k>x[mid2]):
        l=mid2+1
    else:
        l=mid1+1
        r=mid2-1
if(flag==1):
    print("element found at",pos)
else:
    print("element not found")



        
