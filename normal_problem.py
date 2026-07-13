t = int(input())
for i in range(t):
    s = input()
    right = len(s)-1
    b = ""
    for k in range(len(s)):
        if s[right] == 'p':
            b += 'q'
        elif s[right] == 'q':
            b += 'p'
        else:
            b += "w"
        right -= 1
    print(b)
