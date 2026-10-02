t =int(input())
for i in range(t):
    s = input()

    first = 0
    last = 0 

    first += int(s[0])
    first += int(s[1])
    first += int(s[2])
    last += int(s[-1])
    last += int(s[-2])
    last += int(s[-3])

    if first == last :
        print("YES")
    else:
        print("NO")
    
