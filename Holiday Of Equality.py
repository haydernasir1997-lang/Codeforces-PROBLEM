t = int(input())
nums = list(map(int,input().split()))
x = max(nums)
sum = 0
for i in nums:
    sum += x-i
print(sum)
