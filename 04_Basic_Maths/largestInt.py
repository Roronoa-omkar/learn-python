#arr[1,3,5,8] -->largest integer is 8
print("using normal function")
def largest_element(arr):
    arr_sorted = sorted(arr)          #O(nlogn)
    return arr_sorted[-1]

nums = [3,4,5,5,9]
# print(largest_element(nums))

print("No Function use")
nums.sort()   # sorts in place
# print("Largest:", nums[-1])

print("using Recursion")
def recursive_sort(arr, n):
    if n == 1:
        return
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    recursive_sort(arr, n - 1)

nums = [3, 7, 2, 9, 5]
recursive_sort(nums, len(nums))
# print("Largest:", nums[-1])

print("optimal solution")

nums = [2,3,4,5,3,33]

largest_element = nums[0]
for num in nums:
    if num > largest_element:   #O(n) 
        largest_element = num


print(largest_element)

def find_largest(nums):
    largest = nums[0] 

    for num in nums:
        if num> largest:
            largest = num

    return largest

nums = [3, 7, 2, 9, 5]
print(find_largest(nums))
