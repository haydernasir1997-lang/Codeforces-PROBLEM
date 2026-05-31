n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

count = 0
for i in arr:
    if i[1] - i[0] >= 2:
        count+=1
print(count)
