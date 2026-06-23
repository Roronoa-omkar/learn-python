#looking for the array without using hashing 
number = 1 
def my_function(number,arr_list):
    counter = 0
    for item in arr_list:
        if item == number:
            counter += 1
    return counter

target = 1
number_list = [1,2,5,6,1,4,1]

total_matches = my_function(target,number_list)
print(total_matches)