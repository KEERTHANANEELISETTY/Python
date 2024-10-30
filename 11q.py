s=input()
sc=0
hc=0
for i in s:
    if(i=='*'):
        sc+=1
    if(i=='#'):
        hc+=1
print(sc-hc)
        
