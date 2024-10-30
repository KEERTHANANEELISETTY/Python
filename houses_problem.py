'''l=list(map(int,input().split()))
odd=0
even=0
for i in range(0,len(l),2):
    odd+=l[i]
for i in range(1,len(l),2):
    even+=l[i]
print(max(even,odd)) '''

l=list(map(int,input().split()))
s=0
f=0
while(sum(l)!=0):
    ma=max(l)
    s+=ma
    ind=l.index(ma)
    l[ind]=0
    if ind-1>=0:
        l[ind-1]=0
    if ind+1<=len(l)-1:
        l[ind+1]=0
    print(l)
print(s)


