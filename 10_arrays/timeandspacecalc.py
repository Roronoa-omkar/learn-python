import sys
import timeit
mylist1 = ['cherry', 23, True]
mytuple = ('mango', 93, False)
# print(sys.getsizeof(mylist1), "Bytes")
# print(sys.getsizeof(mytuple), "Bytes")

print(timeit.timeit(stmt="[10, 1, 3, 89]", number=1000000))
print(timeit.timeit(stmt="(1, 89, 23, 22, 222)", number=1000000))