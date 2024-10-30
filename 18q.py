s=input()
x=list(s)
for i in range(len(x)):
    if(x[i]=='1'):
        f=i
        break
for i in range(len(s)-1,-1,-1):
    if(s[i]=='1'):
        l=i
        break
print(l-f-1)

