def rotate_array(arr, n):
    # Step 1: Pehle element ko temp variable mein store karo
    temp = arr[0]
    
    # Step 2: Sabhi elements ko ek position left shift karo
    for i in range(1, n):
        arr[i - 1] = arr[i]
        
    # Step 3: Temp element ko last position par daal do
    arr[n - 1] = temp
    
    return arr