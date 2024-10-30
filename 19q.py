import collections
n=int(input())
x=list(map(str,input().split()))
res=collections.Counter(x)
print(res)
for i,j in res.items():
    if j%2!=0:
        print(i)
        break
