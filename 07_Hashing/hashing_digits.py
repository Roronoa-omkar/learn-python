#taking input 
n = int(input("Enter the number of "))
arr = []
for i in range(n):
    element = int(input(f"Enter the element {i} "))
    arr.append(element)

#pre computing the hash 
hash_arr = [0] * 13
for i in range(n):
    hash_arr[arr[i]] += 1


#for every query the number
q = int(input("Enter the number of queries"))
while q>0:
    q = q -1
    number = int(input("Enter the numbers "))
    #fetch 
    print(hash_arr[number])

