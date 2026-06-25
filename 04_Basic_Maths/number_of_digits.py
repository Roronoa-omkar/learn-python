#sample input 156
#output - 3 ( count the digit)

# def digit(N):
#     count = 0
#     while(N>0):
#         last_digit = N % 10  #This will give us 6 - 5 - 1 
#         print(last_digit)
#         count += 1
#         N = N // 10
#     return count 

from math import log10
def value(N):
    count = int(log10(N)) + 1
    return count




t = int(input("Enter the number of test cases: "))
for _ in range(t):
    number = int(input("Enter the nubmer: "))
    print(value(number))
    

 
