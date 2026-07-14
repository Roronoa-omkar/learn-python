def brute_force(arr: list[int]) -> list[int]:
    stack = []
    reversed_arr = []
    for value in arr:
        stack.append(value)
    while len(stack) > 0:
        last_item = stack.pop()
        reversed_arr.append(last_item)
    return reversed_arr
nums = [3,2,5,6]
#print(brute_force(nums))

def better_approach(arr: list[int]) -> list[int]:
    reversed_arr = []
    while len(arr) > 0:
        last_item = arr.pop()
        reversed_arr.append(last_item)
    return reversed_arr
nums = [3, 2, 5, 9]
#print(better_approach(nums))

# nums = [4,5,6]
# reversed_nums = nums[::-1]
# print(reversed_nums)
# for num in reversed(nums):
#     print(num)

def optimized(arr: list[int]) -> None:
    start = 0
    end = len(arr)-1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
if __name__ == "__main__":
    nums = [2, 4, 6]
    optimized(nums)
    #print(nums)
    
#Function were size is explicitly hard-coded
def reverse(arr: list[int], sz: int) -> None:
    start = 0
    end = sz-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
nums = [4, 7, 12, 90]
sz = 4
print(reverse(nums,sz))