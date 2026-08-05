def brute(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
nums = [2, 9, 17, 40]
target = 57
# print(brute(nums, target))

def optimize(nums, target):
    i, j = 0, len(nums) -1
    while(i < j):
        two_sum = nums[i] + nums[j]
        if two_sum > target:
            j -= 1
        elif two_sum < target:
            i += 1
        else:
            return [i, j]
#print(optimize(nums, target))

    