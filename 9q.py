str1=input()
n=int(input())
x=['mon','tue','wed','thu','fri','sat','sun']
s=x.index(str1)+1
cs=0
while(n>0):
    if(s==len(x)):
       s=0
    if(x[s]=='sun'):
       cs+=1
    s+=1
    n-=1
print(cs)
    
