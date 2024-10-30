import math
n,k=map(int,input().split())
s=0
for i in range(0,k+1,2):
    x=math.factorial(n)
    y=math.factorial(n-i)
    z=math.factorial(i)
    c=x/(y*z)
    print(c)
    s+=c
    print(s)
ans=(s%((10**9)+7))
print(ans)
    
    
