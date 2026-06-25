def crown(n):
    for i in range(1, n + 1):
        # 1. Left numbers (1 to i)
        for j in range(1, i + 1):
            print(j, end="")
        
        # 2. Spaces (creates the 'crown' gap)
        print(" " * (2 * (n - i)), end="")
        
        # 3. Right numbers (i down to 1)
        for j in range(i, 0, -1):
            print(j, end="")
            
        print() # New line after each row

# Example usage:
crown(4)