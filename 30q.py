n=int(input())
s=str(n)
es=0
os=0
for i in range(len(s)):
    if(i%2==0):
        es+=int(s[i])
    else:
        os+=int(s[i])
print(abs(os-es))

