t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    for i in nums:
        if nums.count(i) == 1:
            print(nums.index(i)+1)


