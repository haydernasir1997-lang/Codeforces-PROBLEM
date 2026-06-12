n,m = map(int,input().split())
k = m-1
counts = 0
for i in range(n):
    if counts == 2:
        print(f"{"#"}{"."*k}")
        counts = 0
    elif i % 2 == 0:
        print("#"*m)
        counts += 1
    elif i % 2 != 0:
        print(f"{"."*k}{"#"}")       
