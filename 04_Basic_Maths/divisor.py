# def divisor(n):
#     for i in range(1,n+1):
#         if (n%i == 0):
#             print(i)
#     return

# divisor(36)

# def divisor(n):
#     divisors = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             divisors.append(i)
#     return divisors

# print(divisor(36))

#Other solution
from math import sqrt
def divisor(n):
    divisor = []
    for i in range(1,sqrt(n+1)):
        if (n%i == 0):
            divisor.append(i)
        if (n/i) != i:
            divisor.append(n/i);
    sorted(divisor)

print(float(divisor(36)))

# Your function has a few issues:

# sqrt(n+1) returns a float, but range() needs integers.
# range(1, sqrt(n+1)) should be range(1, int(sqrt(n)) + 1).
# divisor() does not return anything.
# sorted(divisor) does nothing unless you assign it.
# print(float(divisor(36))) tries to convert a list to a float.
# n/i gives floats in Python 3; divisors should usually be integers (n//i).

# Here’s a corrected version:

from math import sqrt

def divisor(n):
    divisors = []

    #O(sqrt(n))
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)

            if n // i != i:
                divisors.append(n // i)
    #O(n logn) - n is number of factors
    divisors.sort()
    return divisors
#O(number of factors)
print(divisor(36))

print(len(divisor(36)))
#If you wanted the number of divisors instead of the list itself, use:
