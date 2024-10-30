n=int(input())
e=list(map(int,input().split()))
l=list(map(int,input().split()))
s=0
y=[]
for i in range(n):
    s=s+e[i]
    s=s-l[i]
    y.append(s)
maximum=max(y)
print(maximum)
