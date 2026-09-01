n = int(input())
days = list(map(int,input().split()))
count = 0
while count <= n:

    for i in range(len(days)):
        if n >= 0:
            n -= days[i]
            if n <= 0:
                print(i+1)
                exit()

