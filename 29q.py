n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    if(n2>=100):
        print("%03d" %i,end=" ")
    elif(n2>=10):
        print("%02d" %i,end=" ")
    else:
        print("%0d" %i,end=" ")

        
'''a=12345
print("%d" %a)
print("%05d" %a)
print("%06d" %a)'''
