n = int(input())
for i in range(n):
    lists = []
    a,b,c = map(int,input().split())
    lists.append(a)
    lists.append(b)
    lists.append(c)
    srt = sorted(lists)
    print(srt[1])
