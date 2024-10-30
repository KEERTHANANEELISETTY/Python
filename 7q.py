n=int(input())
pro=1
while n>0:
    d=n%10
    pro=pro*d
    n=n//10
print(pro)
