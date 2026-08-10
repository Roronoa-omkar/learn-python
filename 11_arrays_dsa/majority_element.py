def brute(arr):
    for i in range(len(arr)):
        freq = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                freq += 1
        if freq >= len(arr) // 2:
            return arr[i]
    return -1

def better(arr):
    arr.sort()
    n = len(arr)
    freq = 1
    ans = arr[0]

    for i in range(1, n):
        if arr[i] == arr[i-1]:
            freq += 1
        else:
            freq = 1
        if freq > n/2:
            return arr[i] # majority element
    return ans

def moores(arr):
    freq = 0 
    ans = None

    for num in arr:
        if freq == 0:
            ans = num
        if  num == ans:
            freq += 1
        else:
            freq -= 1
    if arr.count(ans) > len(arr) // 2:
        return ans
    return -1



arr = [1, 1, 2, 2, 2, 2, 2, 3]
print(moores(arr))

