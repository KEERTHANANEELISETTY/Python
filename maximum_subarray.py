n=int(input())
x=list(map(int,input().split()))
s=x[0]
for i in range(0,n):
    cs=0
    for j in range(i,n,1):
        cs+=x[j]
    #print(cs)
    if(cs>s):
        s=cs
        ini=i
print(s)
