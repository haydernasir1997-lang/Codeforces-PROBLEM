t = int(input())
 
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
 
    odd = []
    even = []
 
    for x in nums:
        if x % 2:
            odd.append(x)
        else:
            even.append(x)
 
    if len(odd) % 2 == 0:
        print("YES")
    else:
        found = False
 
        for x in odd:
            for y in even:
                if abs(x - y) == 1:
                    found = True
                    break
            if found:
                break
 
        print("YES" if found else "NO")
      
