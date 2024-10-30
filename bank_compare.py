import math
p=int(input())
t=int(input())
ns=int(input())
ban=[]
for i in range(0,2):
    cv=0  #calculated value
    for i in range(ns):
        ti,roi=map(float,input().split())
        emi=p*roi/(1-1/pow((1+roi),ti*12))
        cv+=emi
    ban.append(cv)
print(ban)
if(ban[0]<ban[1]):
    print("Bank A")
else:
    print("Bank B")
    
        
    
