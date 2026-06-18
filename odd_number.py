n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    if a != b and b == c:
        print(a)
    elif b != a and a == c:
        print(b)
    elif c != a and a == b:
        print(c)    
