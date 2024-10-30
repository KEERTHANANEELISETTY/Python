import math
p=int(input())
r=int(input())
t=int(input())
to=0
while(t):
    to=to+p
    #print(to)
    i=(r*to)/1200
    #print(i)
    to+=i
    t-=1
print(math.ceil(to))

