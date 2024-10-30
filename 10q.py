v=int(input())
w=int(input())
if(2>=w or w%2!=0 or v>w):
    print("INVALID INPUT")   
else:
    x=4*v
    y=x-w
    tw=y//2
    fw=v-tw
print("two wheelers",tw)
print("four wheelers",fw)
