n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for x in l:
    a=x-k
    b=x+k
    for j in l:
        if ((j>=a and j<=b) and (j!=x)):
            c+=1
            break
print(c)


'''another method

n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for x in l:
    a=x-k
    b=x+k
    for j in l:
    if(j==x):
        continue
    if ((j>=a and j<=b):
        c+=1
        break
print(c)'''
