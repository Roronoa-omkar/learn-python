#All Star Pattern
def pattern(N):
    for i in range(N):
        print("* " * N)

t = int(input("Enter number of test cases: "))

for i in range(t):
    number = int(input("Enter a number: "))
    pattern(number)
    print()