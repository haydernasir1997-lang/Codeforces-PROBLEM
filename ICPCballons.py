t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    ans = ""
    count = 0
    for k in range(len(s)):
        if s[k] not in ans:
            count += 2
            ans += s[k]
        else:
            count += 1
            ans += s[k]

    print(count)
