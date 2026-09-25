a,b,c = map(int,input().split())
place = [a,b,c]
place.sort()
sums = (place[1] - place[0]) + (place[2] - place[1])
print(sums)
