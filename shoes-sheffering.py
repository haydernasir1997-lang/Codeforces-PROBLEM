import sys

def solve():
    # Read all inputs from standard input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    output = []
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        # Read the shoe sizes
        s = input_data[idx : idx + n]
        idx += n
        
        p = [0] * n
        i = 0
        possible = True
        
        while i < n:
            j = i
            # Find the contiguous block of identical shoe sizes
            while j < n and s[j] == s[i]:
                j += 1
            
            # If any shoe size belongs to only one person, it's impossible
            if j - i == 1:
                possible = False
                break
            
            # Circular shift the indices for this group (1-based index)
            for k in range(i, j):
                if k == j - 1:
                    p[k] = i + 1   # Last element wraps around to the first
                else:
                    p[k] = k + 2   # Others take the next person's shoes
                    
            i = j
            
        if not possible:
            output.append("-1")
        else:
            output.append(" ".join(map(str, p)))

    # Print all answers separated by a newline
    print("\n".join(output))

if __name__ == '__main__':
    solve()
