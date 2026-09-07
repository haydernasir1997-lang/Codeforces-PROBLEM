n = int(input())
string = input()
s = ""

count = 0
step = 1

while count < len(string):
    s += string[count] 
    count += step 
    step += 1

print(s)
    
        
