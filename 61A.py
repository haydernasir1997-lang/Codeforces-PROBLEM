s = input()
n = input()
arr = ""
for i in range(len(s)):
    if s[i] != n[i]:
        arr += '1'
    else:
        arr += '0' 

print(arr)
