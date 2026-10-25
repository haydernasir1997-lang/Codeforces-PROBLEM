t = int(input())

for i in range(t):
    n = int(input())
    s = input()


    left = 0 
    right = len(s) - 1

    for i in range(n):
        if s[i] == 'B':
            left = i
            break

    for i in range(n):
        if s[right] == 'B':
            break
        else:
            right -= 1

    print((right-left)+1)









