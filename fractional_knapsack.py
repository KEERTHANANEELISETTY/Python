'''n=int(input())
p=list(map(int,input().split()))
w=list(map(int,input().split()))
cap=int(input())
mp=0
index=[i for i in range(n)]
print(index)
pw=[i/j for i,j in zip(p,w)]
print(pw)
index.sort(key=lambda i:pw[i],reverse=True)
print(index)
fr=[0]*n
for i in index:
    if(cap>=w[i]):
        mp+=p[i]
        cap-=w[i]
        fr[i]=1
    else:
        mp+=p[i]*cap/w[i]
        fr[i]=cap/w[i]
print(mp)
print(fr)'''


n=int(input())
knap=[]
for i in range(n):
    p,w=map(int,input().split())
    knap.append([p,w])
cap=int(input())
print(knap)
mp=0
index=[i for i in range(n)]
print(index)
pw=[d[0]/d[1] for d in knap]
print(pw)
index.sort(key=lambda i:pw[i],reverse=True)
print(index)
fr=[0]*n
for i in index:
    if(cap>=knap[i][1]):
        mp+=knap[i][0]
        cap-=knap[i][1]
        fr[i]=1
    else:
        mp+=knap[i][0]*cap/knap[i][1]
        fr[i]=cap/knap[i][1]
print(mp)
print(fr)
