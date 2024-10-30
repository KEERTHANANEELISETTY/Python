n,le=map(int,input().split())
sum=0
if((n>2 and n<10) and (le>1 and le<20)):
    for i in range(le):
        sum+=n
        n-=1
    print(sum)
else:
    print("invalid input")
        
