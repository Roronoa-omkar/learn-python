def largest(nums):
    largest = nums[0]
    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]
    return largest

def second_largest(nums):
    nums.sort()
    largest = nums[len(nums)-1]
    for i in range(len(nums)-2,-1,-1):
        if arr[i] != largest:
            largest = arr[i]
            break
    return largest

def second_largest_better(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    second_largest = -1 # or float('-inf')
    for num in nums:
        if (num > second_largest and num < largest):
            second_largest = num
    return second_largest





arr = [4, 7, 7, 1, 6]
print(second_largest_better(arr))
