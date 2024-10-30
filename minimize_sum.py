n=int(input())
k=int(input())
l=list(map(int,input().split()))
print(l)
for i in range(k):
    m=max(l)
    for i in range(n):
        if l[i]==m:
            l[i]=m//2
    print(l)
print(int(sum(l)))
