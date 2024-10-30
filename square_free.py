import math
def ps(nu):
    x=math.floor(math.sqrt(nu))
    if(x*x==nu):
        return 1
    else:
        return 0
n=int(input())
l=[]
l.append(1)
for i in range(2,(n//2)+1):
    if n%i==0:
        l.append(i)
print("l",l)
psl=[]
c=0
for i in range(1,len(l)):
    x=ps(i)
    if(x==1):
        psl.append(i)
print("ps",psl)
a=set(l)
b=set(psl)
c=a-b
print("c" ,c)
c=list(c)
b=list(b)
count=0
for i in c:
    flag=1 # considered for counting
    for j in range(1,len(b)):
        if (i%b[j]==0):
            flag=0 # not consider for counting
            break
    if flag==1:
        count+=1
print(count)



