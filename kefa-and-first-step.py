import sys

def solve():
    # Read all lines from standard input
    input = sys.stdin.read
    data = input().split()
    
    # If there is no input, exit
    if not data:
        return
        
    n = int(data[0])
    a = [int(x) for x in data[1:]]
    
    max_len = 1
    current_len = 1
    
    # Iterate through the sequence starting from the second element
    for i in range(1, n):
        if a[i] >= a[i-1]:
            current_len += 1
        else:
            current_len = 1
            
        # Update maximum length found so far
        if current_len > max_len:
            max_len = current_len
            
    print(max_len)

if __name__ == '__main__':
    solve()
