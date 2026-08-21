# arr = [2, 3, 3, 3, 5, 5]
# unique_set  = set()
# for i in arr:
#     unique_set.add(i)
# sorted_unique = sorted(unique_set)

# #To overwrite the array using the sorted unique set()
# index = 0
# for val in sorted_unique:
#     arr[index] = val
#     index += 1
# print(index)
# print(unique_set)
# print(sorted_unique)

def remove_duplicates(nums):
    if not nums:
        return 0
    
    i = 0  # Slow pointer (hamesha unique elements ke end par rahega)
    
    for j in range(1, len(nums)):  # Fast pointer (array ko scan karega)
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
            
    return i + 1  # Unique elements ka count

arr = [1,1,2,3,5,5,5,10]
print(remove_duplicates(arr))
