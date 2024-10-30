n=int(input())
s=list(map(int,input().split()))
f=list(map(int,input().split()))
f1=f.copy()
f.sort()
s1=[]
for i in f:
    x=i
    xi=f1.index(x)
    s1.append(s[xi])
    f1[xi]=0
print(s1)
print(f)
na=1
i=0
re=[]
for j in range(1,n):
    if(s1[j]>=f[i]):
        na+=1
        i=j
        re.append(j)
print(na)
print(re)
