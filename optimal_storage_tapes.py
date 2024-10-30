'''n=int(input())
x=list(map(int,input().split()))
x.sort()
mrt=0
for i in range(n):
    cs=0
    for j in range(0,i+1):
        cs+=x[j]
    print(cs)
    mrt+=cs
    print(mrt)
print(mrt//n)
'''

import itertools
n=int(input())
x=list(map(int,input().split()))
y=list(itertools.permutations(x))
y.sort()
print(y)
print(y[0])
z=y[0]
for i in z:
    a=i[0]


