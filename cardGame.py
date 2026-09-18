table = input()
strings = list(input().split())
for i in range(len(strings)):
    if table[0] in strings[i] or table[1] in strings[i]:
        print("YES")
        break
else:
    print("NO")


