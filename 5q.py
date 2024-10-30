n=int(input())
l=[]
for i in range(n):
    a=int(input())
    if a not in l:
        l.append(a)
    else:
        while(1):
            a=a+1
            if a not in l:
                l.append(a)
                break
print(l)
print(sum(l))
