n = int(input())
s1 = "I hate that "
s2 = "I love that "
s3 = "I hate it"
for i in range(1,n+1):
    if i == n and i % 2 != 0: 
        print("I hate it")
    elif i == n and i % 2 == 0: 
        print("I love it")    
    elif i % 2 == 0:
        print("I love that",end=" ")
    elif i % 2 != 0 :
        print("I hate that" ,end=" ")
       


