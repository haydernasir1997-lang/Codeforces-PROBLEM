n , h = map(int,input().split())

m = input().split()

arr = []
counts = 0

for i in range(n):
    arr.append(int(m[i]))
for i in arr:
    if i > h:
        counts+=1
print(len(arr) + counts)        


