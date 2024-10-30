s=input()
str2=""
n=len(s)
i=0
while(n>i):
    if(s[i]=='G' or s[i]=='&'):
        i+=1
        continue
    if(s[i]=='E' and s[i+1]=='F'):
        i+=2
        continue
    if(s[i]=='5' and s[i+1]=='6'):
        i+=2
        continue
    str2+=s[i]
    i+=1
print(str2)
            
