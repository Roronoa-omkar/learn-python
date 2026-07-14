def brute_force(arr):
    max_sum = float('-inf')
    for i in range(len(arr)):
        current_sum = 0 
        for j in range(i, len(arr)):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return max_sum
nums = [1, -2, -3, 4, 5]
#print(brute_force(nums))

def optimize(arr):
    current_sum = 0
    max_sum = float('-inf')
    for i in range(len(arr)):
        current_sum += arr[i]
        max_sum = max(current_sum, max_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum
#print(optimize(nums))
