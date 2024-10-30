n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(k):
    l=l[n-1:]+l[0:n-1]
    print(l)
