t = int(input())
 
for _ in range(t):
    n = 10
    grid = []
 
    for i in range(n):
        grid.append(input())
 
    ans = 0
 
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'X':
                score = min(i, j, 9 - i, 9 - j) + 1
                ans += score
 
    print(ans)
