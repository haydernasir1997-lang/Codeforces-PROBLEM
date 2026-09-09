t = int(input())

for _ in range(t):
    n = int(input())
    s = input().lower()

    result = ""

    for letter in s:
        if not result or letter != result[-1]:
            result += letter

    if result == "meow":
        print("YES")
    else:
        print("NO")
