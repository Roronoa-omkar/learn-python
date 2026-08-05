# Step 1: Initialize the hash table with 256 zeros
hash_table = [0] * 256

# Step 2: Read input string and pre-compute frequencies
input_string = input()

for char in input_string:
    ascii_value = ord(char)
    hash_table[ascii_value] += 1

# Step 3: Convert the number of queries to an integer
total_queries = int(input())

# Step 4: Loop through each query
while total_queries > 0:
    # Read the target character inside the loop
    target_char = input()
    
    # Get its ASCII value and print its pre-computed count
    ascii_value = ord(target_char)
    print(hash_table[ascii_value])
    
    # Decrement loop counter
    total_queries -= 1
