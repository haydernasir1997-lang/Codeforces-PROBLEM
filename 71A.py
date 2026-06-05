n = int(input())
counts = 0

for i in range(n):
    s = input()
    l = len(s)
    if l <= 10:
        print(s)
    else:
        print(f"{s[0]}{len(s)-2}{s[-1]}")
