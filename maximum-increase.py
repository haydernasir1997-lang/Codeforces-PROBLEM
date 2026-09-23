n = int(input())
nums = list(map(int, input().split()))

current = 1
maximum = 1

for i in range(1, n):
    if nums[i] > nums[i - 1]:
        current += 1
    else:
        current = 1

    maximum = max(maximum, current)

print(maximum)
