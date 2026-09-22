t = int(input())


for i in range(t):
    s = input()

    count = 0
    word = "codeforces"
    for k in range(len(word)):
        if word[k] != s[k]:
            count += 1
    print(count)

