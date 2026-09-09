t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    nums = [a,b,c]
    nums.sort()
    count = 0
    while len(set(nums)) == len(nums):
        nums[-1] -= 1
        nums[0] += 1
        count += 1
    print(count)
