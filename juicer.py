n , b , d = map(int, input().split())
size = list(map(int, input().split()))

west = 0
count = 0

for i in size:

    if i > b:
        continue

    west += i

    if west > d:
        count += 1
        west = 0
        

print(count)
    
