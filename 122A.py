n = int(input())
s = str(n)

counts = 0
lucky = "47"

for i in s:
    if i in lucky:
        counts += 1

if len(s) == counts or n % 4 == 0 or n % 7 == 0 or n % 47 == 0 or n % 74 == 0 :
    print("YES")
else:
    print("NO")
