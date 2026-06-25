#reading a static array 
def reading(length , capacity , arr , element):
    if length < capacity:
        arr[length] = element
        length += 1 

#removing from last in static array 
def removing(length,capacity,arr):
    if length > 0:
        arr[length - 1] = 0
        length -= 1
    return arr , length

#inserting in static array
def insertMiddle(arr, index, element, length, capacity):
    if length < capacity:
        for i in range(length - 1, index - 1, -1):
            arr[i + 1] = arr[i]
        arr[index] = element 
        length = length + 1
    return arr, length

#removing middle element in static array
def removeMiddle(arr , index , length):
    for index in range(index+1,length):
        arr[index - 1] = arr[index]
        arr[index -1] = 0

my_arr = [10,20,30,0,0]
removeMiddle(my_arr, 1, 3)
print(my_arr)