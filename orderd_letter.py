s1 = input()
s2 = input()
target = input()

if sorted(s1 + s2) == sorted(target):
    print("YES")
else:
    print("NO")
