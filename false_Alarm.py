t = int(input())
for i in range(t):
    n , x = map(int,input().split())
    doors = list(map(int,input().split()))

    
    for i in range(len(doors)):
        if doors[i] == 1:
            first = i
            break

    for j in range(len(doors)-1 ,-1 ,-1):
        if doors[j] == 1:
            last = j
            break

    if (j-i+1) <= x:
        print("YES")
    else:
        print("NO")
