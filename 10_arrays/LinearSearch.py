def liner_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

nums = [1,5,3,9]
target = 9
print(liner_search(nums, target))
