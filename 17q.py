import collections 
s=input()
x=s.split()
y=collections.Counter(x)
print(y)
c=0
for i,j in y.items():
    if j==1:
        c+=1
print(c)
    
