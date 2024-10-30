n=int(input())
x=list(map(int,input().split()))
b=[]
for i in x:
    a=bin(i)
    b.append(a)
print(b)
boc=[]
for i in b:
    x=i.count('1')
    boc.append(x)
print(boc)
c=0
for i in range(0,n-1,1):
    for j in range(i+1,n,1):
        if(boc[i]>boc[j]):
            c+=1
            print(boc[i],boc[j])
print(c)

    
    
    
