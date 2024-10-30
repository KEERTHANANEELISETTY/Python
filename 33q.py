l=list(map(int,input().split()))
fee=0
for i in l:
    if(i<=0 or i>120):
        print("Invalid input")
        break
    else:
        if(i<17):
            fee+=200
        elif(i>=17 and i<40):
            fee+=400
        else:
            fee+=300
print(fee)
        
