n=int(input())
a=[]
d=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append(x)
    d.append(y)
c=a.copy()
c.sort()
pfc=0
dc=0
v=c[0]
ai=a.index(v)
dc=v+d[ai]
print(dc)
pfc+=1
dl=[]
for j in range(1,n):
    v=c[j]
    if (v>=dc):
        pfc+=0
    else:
        ai=a.index(v)
        dc=v+d[ai]
        for i in range(v,dc+1):
            dl.append(i)
        if v in dl or v+dc in dl:
            pfc+=1
    print(dc)
print(pfc)


'''n=int(input())
l1=[]
l2=[]
l3=[]
pc=0
for i in range(n):
    a,b=map(int,input().split())
    l1.append(a)
    l2.append(b)
    x=sorted(l1)
for i in x:
    index=l1.index(i)
    y=l2[index]
    pst=i+y
    l3.append(pst)
    z=min(l3)
    if z<pst+1:
        break
    else:
        pc+=1
print(pc)'''

        
