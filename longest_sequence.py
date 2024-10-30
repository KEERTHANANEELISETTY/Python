n=int(input())
l=list(map(int,input().split()))
psl=[]
i=0
ans=[]
psl.append(l[i])
while(i<n-1):
    if(l[i+1]>=l[i]):
        psl.append(l[i+1])
    else:
        # print(psl)
        ans.append(psl)
        psl=[]
        psl.append(l[i+1])
    i+=1
ans.append(psl)
#print(psl)
#print(ans)
maxlen=[]
for i in ans:
    a=len(i)
    maxlen.append(a)
ma=max(maxlen)
mli=maxlen.index(ma)
print(ans[mli])
    
    
    
    
    

    
