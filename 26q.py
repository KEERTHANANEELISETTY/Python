t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    count += n // 10
    n %= 10
    count += n // 7
    n %= 7
    count += n // 5
    n %= 5
    count += n
    print(count)

'''n=int(input())
c=0
flag=0#calculation done
if(n==1 or n==5 or n==7 or n==10):
    ans=1
    flag=1#no calculation done
elif(n<10):
    rem=n
if(n>=10):
    c=c+n//10
    rem=n%10
if(rem>=7):
    c=c+rem//7
    rem=rem%7
if(rem>=5):
    c=c+rem//5
    rem=rem%10
if(rem>=1 and rem<5):
    c=c+rem
if(flag==1):
    print(ans)
else:
    print(c)'''
    
    
