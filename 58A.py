n = input()

word = "hello"
count = 0

for i in n:
    if count < len(word) and i == word[count]:
        count += 1

if count == len(word):
    print("YES")
else:
    print("NO")
    
