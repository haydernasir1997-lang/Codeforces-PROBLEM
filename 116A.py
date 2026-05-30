n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

sum = 0
m = []

for i in range(len(arr)):
    
    sum = (sum - arr[i][0]) + arr[i][1]
    m.append(sum)

print(max(m))



