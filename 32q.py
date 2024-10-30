n=int(input())
l=list(map(int,input().split()))
c=1
ans=l[0]
print(ans)
for i in range(1,n):
    if(ans<=l[i]):
        print(l[i])
        c+=1
print(c)


'''n=int(input())
l=list(map(int,input().split()))
c=1
for i in range(1,n,1):
    flag=0
    for j in range(i-1,-1,-1):
        if(x[j]>x[i]):
            flag=1
            break
    if(flag==0):
        c+=1
    print(x[i])
print(c)'''
            
