def prime(nu):
    flag=0 #third factor not identified
    for i in range(2,(nu//2)+1):
        if nu%i==0:
            flag=1 #third factor identified
            break
    if flag==1 or nu==1:
        print("None")
    else:
        print(nu)
import math
n=int(input())
l=list(map(int,input().split()))
mi=min(l)
l.remove(mi)
lcm_l=math.lcm(*l)
nu=lcm_l+mi
prime(nu)

