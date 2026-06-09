m = int(input())
n = input().lower()
s = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(s)):
    if s[i] not in n :
        print("NO")
        break
else:
    print("yes")        

    
