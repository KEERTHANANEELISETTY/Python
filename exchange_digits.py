from itertools import permutations
a,b=map(int,input().split())
a=sorted(list(str(a)))
x=permutations(a)
l=[]
flag=0
for i in x:
    s=''
    for j in i:
        s+=j
        y=int(s)
        if(y>b):
            l.append(y)
            flag=1  # if any elememt is greater than 'b' flag becomes 1
if(flag==0):
    print(-1)
else:
    print(l) # list contains the elements greater than b 
    c=min(l)
    print(c)

