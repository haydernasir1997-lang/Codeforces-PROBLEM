t = int(input())
for i in range(t):
    a , b = map(int,input().split())
 
    c = (a+b)//2
 
    ans = (c-a) + (b-c)
 
    print(ans)
    
 
 
