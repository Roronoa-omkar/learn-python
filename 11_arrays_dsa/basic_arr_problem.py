def calculate(arr: list[int]) -> None:
    sum = 0 
    product = 1
    for value in arr:
        sum += value
        product *= value
    return sum, product
nums = [2, 4, 6]
#print(calculate(nums))

def swap(arr: list[int]) -> None:
    if len(arr) < 2:
        return None
    min_index = 0
    max_index = 0

    for i in range(len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
        if arr[i] > arr[max_index]:
            max_index = i
    arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
nums = [45, 8, 1, 0, 56]
swap(nums)
#print(nums)


#WAF print unique elements 
def unique(arr: list[int]) -> None:
    unique_nums = []
    for value in arr:
        if value not in unique_nums:
            unique_nums.append(value)
    return unique_nums
nums = [2,2,2,2,2,3,3,3,5]
#print(unique(nums))
new_num = list(set(nums))
#print(new_num)


#WAF for intersection of 2 arrays
def intersection(arr1: list[int], arr2:list[int]) -> list[int]:
    set1 = set(arr1)
    set2 = set(arr2)
    result = set1 & set2
    return list(result)
def inter(arr1, arr2):
    result = []
    for value in arr1:
        if value in arr2 and value not in result:
            result.append(value)
    return result
nums1 = [1, 2, 2, 1, 3]
nums2 = [2, 2, 3, 5]
#print(intersection(nums1, nums2))
#print(inter(nums1, nums2))


#To print all sub-array in a given array
def subarray(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(i, j+1):
                print(arr[k], end="")
            print(end=" ")
        print()
nums = [1, 4, 9, 8]
# subarray(nums)