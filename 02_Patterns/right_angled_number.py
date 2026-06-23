def pattern(N):
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
test_cases = int(input("Enter the number of test cases: "))
for i in range(test_cases):
    ouput = int(input("Enter the Value: "))
    pattern(ouput) #output here is N or 



