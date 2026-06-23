# #brute force 
# def gcd(n1,n2):
#     for i in range(1,min(n1,n2)+1):
#         if (n1 % i == 0 and n2 %i ==0):
#             current_gcd =i
#     return current_gcd
# value1 = 20 
# value2 = 40 
# print(gcd(value1,value2))

# def gcd(n1, n2):
#     # Start at the minimum value, count backwards to 1
#     for i in range(min(n1, n2), 0, -1):
#         if n1 % i == 0 and n2 % i == 0:
#             return i  # The first one found will be the largest
# value1 = 20 
# value2 = 40 
# print(gcd(value1, value2)) # Output will be 20

#optimised 
def gcd(a,b):
    while (a>0 and b>0):
        if(a>b):
            a = a %b
        else:
            b = b % a
    if(a == 0):
        return b 
    else:
        return a

value1 = 52
value2 = 10
print(gcd(value1,value2))        #TC - O(logbase(ɸ)min(a,b))

#or 

def gcd_fast(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

print(gcd_fast(52, 10)) 