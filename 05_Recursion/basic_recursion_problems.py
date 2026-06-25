#print name N time 

# def name(N):
#     if N<=0:
#         return
#     print("omkar")
#     name(N-1) 
# name(5)

# def name(i,N):
#     if i>N:
#         return
#     print("raj")  #TC = O(N) 
#     name(i+1,N)

# name(5,3)


#Factorial

# def factorial(N):
#     if N==1:
#         return 1
#     return N * factorial(N-1)
#     factorial(N-1)


# print(factorial(4))
                    

#Print (1 - N)
# def number(i,N):
#     if i>N:
#         return
#     print(i)
#     number(i+1,N)

# number(1,10)

#Print (N - 1)
# def number(N):
#     if N<0:
#         return
#     print(N)
#     number(N-1)
# number(10)


#Backtracking --> simple terms executing recursion, when print() is written after f(x) call 
# def output(i,N):
#     if i<N:
#         return
#     output(i-1,N)
#     print(i)
# output(5,1)

#Print N - 1

# def backtrack(i, n):
#     if i > n:
#         return
#     backtrack(i+1, n)
#     print(i)

# backtrack(1, 5)