T=int(input())
x=list(map(int,input().split()))
c=0
for i in range(T-1):
    if(x[i]==1):
        continue
    for j in range(i+1,T,1):
        if(x[i]==0 and x[j]==1):
            c+=1
            print(i,j)
print(c)
