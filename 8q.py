n=int(input())
lis=[]
ms=0
for i in range(n):
    b=int(input())
    lis.append(b)
for i in range(n):
    su=lis[i]
    for j in range(i,(n-1),1):
        if(lis[j]<lis[j+1]):
            su+=lis[j+1]
        else:
            break
    if ms<su:
        ms=su
print(ms)

    
