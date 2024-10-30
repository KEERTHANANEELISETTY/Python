n=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
for i in l:
    if(i%10==0):
        x.append(i)
    else:
        y.append(i)
l=y+x
print(l)
        
