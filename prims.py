n=int(input())
m=n
x=[[int(input())for j in range(m)]for i in range(n)]
print(x)
arr=x
INF = 9999999
selectednode = [0]*n
noedge = 0
selectednode[0] = True
ans=0
# printing for edge and weight
print("Edge : Weight\n")
while (noedge < m - 1):
    minimum = INF
    a = 0
    b = 0
    for x in range(m):
        if selectednode[x]:
            for y in range(m):
                if ((not selectednode[y]) and arr[x][y]):  
                    # not in selected and there is an edge
                    if minimum > arr[x][y]:
                        minimum = arr[x][y]
                        a = x
                        b = y
                    
    print(str(a) + "-" + str(b) + ":" + str(arr[a][b]))
    ans=ans+minimum
    selectednode[b] = True
    noedge += 1
print(ans)
