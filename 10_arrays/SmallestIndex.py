#find the smallest index 

def index_smallest(arr):
    small_index = float("inf")
    for i in arr:
        if i < small_index:
            small_index = i
    return small_index
 


nums = [1, -4, 5, 99]
print(index_smallest(nums)) 