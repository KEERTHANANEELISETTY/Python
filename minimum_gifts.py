t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    ge=[]
    ge.append(1)
    for i in range(1,n):
        if l[i]>l[i-1]:
            x=ge[i-1]+1
            ge.append(x)
        else:
            ge.append(1)
r=sum(ge)
print(r)
