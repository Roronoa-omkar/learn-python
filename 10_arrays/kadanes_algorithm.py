#How to get the sub-arrays from an array 
#arr[1, 3, 4, 6]

arr = [ 1, 3, 4, 6]  

for i in range(len(arr)):
    for j in range(i,len(arr)):
        for k in range(i, j+1):
            print(arr[k])

       

    