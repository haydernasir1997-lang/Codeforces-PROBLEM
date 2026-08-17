t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    seen = set()
    count = 0

    for i in range(len(s)):
        seen.add(s[i])
        count += len(seen)
    print(count)

