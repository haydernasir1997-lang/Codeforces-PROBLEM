n = int(input())
a = list(map(int, input().split()))

mx = max(a)
mn = min(a)

# leftmost maximum
max_pos = a.index(mx)

# rightmost minimum
min_pos = n - 1 - a[::-1].index(mn)

ans = max_pos + (n - 1 - min_pos)

if max_pos > min_pos:
    ans -= 1

print(ans)
