def is_odd(x):
    # Returns True if x is odd, False if x is even
    return x % 2 == 1
 
def is_even(x):
    # Returns True if x is even, False if x is odd
    return x % 2 == 0
 
t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
 
    count = 0
    for k in range(len(nums)-1):
        if is_odd(nums[k]) and is_odd(nums[k+1]):
            count += 1
        elif is_even(nums[k]) and is_even(nums[k+1]):
            count += 1
    print(count)
