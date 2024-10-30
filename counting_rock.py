n,r=map(int,input().split())
l_r_s=list(map(int,input().split()))
b=[]
for _ in range(r):
    low,high=map(int,input().split())
    c=0
    for i in l_r_s:
        if(low<=i and i<=high):
            c+=1
    b.append(c)
print(b)
    
        
    
