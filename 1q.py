n=int(input())
x=bin(n)#decimal to binary
print(type(x))
print(x)
x=x[2:]
y=''
for i in x:
    if i=='1':
        y+='0'
    else:
        y+='1'
print(y)
ans=int(y,2)#binary to decimal
print(ans)

    
