'''n1=int(input())
n2=int(input())
count = 0
for i in range(n1, n2 + 1):
    x = str(i)
    if len(x) == len(set(x)):
        count += 1
print(count)'''

n1=int(input())
n2=int(input())
count = 0
for i in range(n1, n2 + 1):
    x = str(i)
    y=[]
    flag=0 #repeated digit is not identified
    for j in x:
        if j not in y:
            y.append(j)
        else:
            flag=1#repeated digit identified
            break
    if(flag==0):
        count+=1
print(count)
        

