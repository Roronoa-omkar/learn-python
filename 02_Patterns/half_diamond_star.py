N = 5

for i in range(0,N):
    for j in range(0,i+1):
        print("*" ,end=" ")
    print()
for i in range(1,N+1):
    for j in range(0,N-i):
        print("*",end=" ")
    for j in range(0,i+1):
        print(" ",end=" ")
    print()

# def pattern(N):
#     for i in range(1,(2*N -1)+1):
#         stars = i
#         if(i>N):
#             stars = 2*N -i
#         for j in range(1,stars+1):
#             print("*",end=" ")
#         print()

# value =5
# pattern(value)





