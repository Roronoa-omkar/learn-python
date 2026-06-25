def pattern(N):
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()
value = 5
pattern(value)