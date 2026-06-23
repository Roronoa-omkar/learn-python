def pattern(N):
    for i in range(0,N):
        #space
        for j in range(0,i):
            print(" ",end="") 
        #star
        for j in range(0,(N-i)*2 - 1):
            print("*",end="")
        #space
        for j in range(0,i):
            print(" ",end="")
        print()


value = 5
pattern(value)