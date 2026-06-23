# def sum(i,s):
#     if(i<1):
#         print(s)
#         return s
#     return sum(i-1,s+i)

#Function call recursion 

def total(n):
    if (n == 0): return 0
    return n + total(n-1)    #TC - O(n), SC - O(n)

print(total(3))

