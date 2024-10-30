import math
r1=int(input())
n=int(input())
r2=int(input())
x=int(input())
nh=math.ceil(x/60)
if(nh>=n):
    c1=n*r1
    c2=(nh-n)*r2
    print(c1+c2)
else:
    c1=nh*r1
    print(c1)
