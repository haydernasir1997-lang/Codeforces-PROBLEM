t = int(input())
for i in range(t):
    n = int(input())
    s = input()
 
    a = 0
    b = 0
    c = 0
    d = 0
 
    for i in range(len(s)):
        if s[i] == 'A' and a < n:
            a += 1
        elif s[i] == 'B' and b < n:
            b += 1
        elif s[i] == 'C' and c < n:
            c += 1
        elif s[i] == 'D' and d < n:
            d += 1
 
    print(a+b+c+d)
