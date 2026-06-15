y = int(input())

y += 1

while True:
    if len(set(str(y))) == len(str(y)):
        print(y)
        break
    y += 1
