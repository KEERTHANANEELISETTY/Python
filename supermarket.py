n,m=map(int,input().split())
c=[]
r=[]
for i in range(n):
    q,p=map(int,input().split())
    c.append([q,p])
for i in range(m):
    q,p=map(int,input().split())
    r.append([q,p])
cust=0
print(c)
print(r)
for i in c:
    a=i[0]
    b=i[1]
    for j in r:
        x=j[0]
        y=j[1]
        if(x>=a and y<=b):
            cust+=1
            break
print(cust)
    
    
