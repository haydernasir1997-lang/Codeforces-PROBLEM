t = int(input())
for i in range(t):
    n = int(input())
    if n < 10:
        print(n-1)
    else:
        first = int(str(n)[0])-1
        print(int(f"{first}" + str(n)[1:] ))
        
