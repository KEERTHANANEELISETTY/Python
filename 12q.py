n=int(input())
l=list(map(int,input().split()))
print(l)
nzl=[]
zl=[]
for i in l:
    if(i!=0):
        nzl.append(i)
    if(i==0):
        zl.append(i)
nzl.extend(zl)
print(nzl)
