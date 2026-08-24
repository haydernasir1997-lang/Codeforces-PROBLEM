t = int(input())
for i in range(t):

    n = int(input())   
    s = input()

    left = 0
    temp = 1

    decrypted = ""

    while temp < len(s):

        if s[left] != s[temp]:
            temp += 1

        elif s[left] == s[temp]:
            decrypted += s[left]
            left = temp + 1
            temp = left + 1
    print(decrypted)
