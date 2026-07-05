# list1 = [10, 20, 30]
# list2 = [100, 200, 300]
# #printing list
# for i, j in zip(list1, list2):
#     print(i, j)


# # A 2x3 matrix
# matrix = [[1, 2, 3], [4, 5, 6]]
# for i in range(len(matrix)):          # Loops through rows
#     for j in range(len(matrix[i])):   # Loops through columns in that row
#         print(i,j)


# number = [10,20,30]
# print(len(number))
# print(10 in number)


#Mutating
arr = [1, 2]
arr.append(3)        # [1, 2, 3]
arr.insert(0, 99)    # [99, 1, 2, 3]  (Inserts 99 at index 0)
arr.extend([4, 5])   # [99, 1, 2, 3, 4, 5] (use it combine two list)


#Removing
arr = ['a', 'b', 'c', 'b']

arr.__delitem__(slice(1,3))
print(arr)