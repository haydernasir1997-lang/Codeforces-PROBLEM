
n = int(input())

s = []
for i in range(n):
    s.append(input())

counts = 1  

for j in range(n - 1):
    if s[j] != s[j + 1]:
        counts += 1

print(counts)

