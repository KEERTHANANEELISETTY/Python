n=int(input())
l=list(map(int,input().split()))
k=int(input())
l=l[k:n]+l[0:k]
print(l)
