#Taking each element as input into the array
arr_size = int(input("Enter the size of your array: "))

arr = []
for i in range(arr_size):
    num = int(input("Enter the elements of arr: "))
    arr.append(num)

#pre computation
hash_table = [0] * 13
for i in arr:
    hash_table[i] += 1



#Total number of queries
queries = int(input("Enter the number of queries "))
for q in range(queries):
    number = int(input("Enter the numbers you want to check: "))
    ##Fetch
    print(hash_table[number])
