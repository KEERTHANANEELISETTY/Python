t=int(input())
for _ in range(t):
    s=input().split()
    d=[]
    c=[]
    re=[]
    l=list(s)
    print(l)
    for i in l:
        if  i.isdigit():
            d.append(i)
        else:
            c.append(i)
    d.sort()
    c.sort()
    print(d)
    print(c)
    for i,j in zip(c,d):
        print(i.lower(),j,end=' ')

    
    
            
        
    
