import math
def prime(nu):
    flag=1 # third factor not identified
    for j in range(2,int(math.sqrt(nu)+1)):
        if(nu%j==0):
            flag=0
            break
    if flag==0:
        return 0
    else:
        return 1
n=int(input())
sum=0
lp=[]
for i in range(2,n+1):
    x=prime(i)
    if x==1:
        lp.append(i)
print(lp)
c=0
for j in range(2,len(lp),1):
    a=lp[j]
    s=0
    for k in lp:
        s+=k
        if (s==a):
            c+=1
            print(a)
            break
        if s>a:
            break
print(c)
        
        
