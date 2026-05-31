for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        if arr[j]==1:
            x , y = i ,j
print(abs(x-2) + abs(y-2))
             
                 

