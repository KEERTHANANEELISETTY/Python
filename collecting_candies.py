t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    a=[]
    sum_x=x[0]
    for i in range(1,n):
        sum_x+=x[i]
        a.append(sum_x)
    print(a)
    print(sum(a))
    
