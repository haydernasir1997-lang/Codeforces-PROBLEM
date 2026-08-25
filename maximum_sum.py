t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
 
    nums.sort()
 
    prefix = [0] * (n + 1)
 
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
 
    ans = 0
 
    for i in range(k + 1):
        left = 2 * i
        right = n - (k - i)
 
        current = prefix[right] - prefix[left]
 
        ans = max(ans, current)
 
    print(ans)
