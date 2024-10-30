'''from itertools import combinations
n=int(input())
l=list(map(int,input().split()))
x=int(input())
tc=combinations(l,3)
flag=0
for i in tc:
    y=sum(i)
    if(y==x):
        flag=1
        break
if(flag==1):
    print("True")
else:
    print("False")
'''

n=int(input())
x=list(map(int,input().split()))
s=int(input())
flag=0
for i in range(n-2):
    a=x[i]
    for j in range(i+1,n-1):
        b=x[j]
        for k in range(j+1,n):
            c=x[k]
            if(a+b+c==s):
                flag=1
                break
        if(flag==1):
            break
    if(flag==1):
        break
if(flag==1):
    print("True")
else:
    print("False")

        
