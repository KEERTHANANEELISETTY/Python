n,k=map(int,input().split(","))
l=[]
l.append(1)
for i in range(2,(n//2)+1,1):
    if(n%i==0):
        l.append(i)
l.append(n)
if(k>len(l)):
    print("1")
else:
    a=l[-k]
    print(a)
        
