t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    minimum = float('inf')

    for i in range(n - 1):
        minimum = min(minimum, nums[i + 1] - nums[i])

    print(minimum)
