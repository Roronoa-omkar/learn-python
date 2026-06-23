# --- STEP 1: GET THE ARRAY ELEMENT BY ELEMENT ---
n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    # We take each number one by one, convert to int, and add to our list
    element = int(input(f"Enter element at index {i}: "))
    arr.append(element)


# --- STEP 2: CREATE THE HASH (TALLY) LIST MANUALLY ---
hash_arr = []
# We manually loop 13 times to fill our tally list with 13 zeros
for i in range(13):
    hash_arr.append(0)


# --- STEP 3: TALLY THE FREQUENCIES ---
for num in arr:
    if num < 13:
        # Look at the current number, find that index in hash_arr, and add 1
        hash_arr[num] = hash_arr[num] + 1


# --- STEP 4: ANSWER THE QUERIES ---
q = int(input("Enter the number of queries: "))
for i in range(q):
    number = int(input("Enter the number to search for: "))
    if number < 13:
        print("Frequency is:", hash_arr[number])
    else:
        print("Frequency is: 0")



# 1. Take elements all at once (Clean input handling)
raw_input = input("Enter all array elements separated by spaces: ")
arr = [int(x) for x in raw_input.split()]

# 2. Pre-computation using a Hash Map (Dictionary)
# This handles numbers of any size (even millions) cleanly.
frequency_map = {}
for element in arr:
    if element in frequency_map:
        frequency_map[element] += 1
    else:
        frequency_map[element] = 1

# 3. Process Queries
queries = int(input("Enter the number of queries: "))
for q in range(queries):
    number = int(input("Enter the number you want to check: "))
    
    # .get(number, 0) fetches the count, or returns 0 if the number isn't in the map
    result = frequency_map.get(number, 0)
    print(f"Result: {result}")        