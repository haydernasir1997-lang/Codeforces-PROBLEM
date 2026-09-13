t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    answer = 0

    for x in range(1, n + 1):
        answer += a.count(x) // 2

    print(answer)
