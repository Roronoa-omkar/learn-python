N = 5
for i in range(1,N+1):
    for j in range(1,N-i+2):
        print(j,end=" ")
    print()

#or 
N = 5
for i in range(0,N):
    for j in range(1,N-i+1):
        print(j,end=" ")
    print()
