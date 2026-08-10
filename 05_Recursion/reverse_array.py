def f(i, arr,n):
    #base case
    if i>= len(arr)//2:
        return
    #logic
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    #recursive call
    f(i+1, arr,n)

if __name__ == "__main__":
    arr = [2, 3, 6, 9]
    n= len(arr)

    f(0, arr, n)
    print(*arr)