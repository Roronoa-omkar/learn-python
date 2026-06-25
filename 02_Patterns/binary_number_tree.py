# def binary(n):
#     for i in range(0,n):  #outer loop keeps the track of rows 
#         for j in range(i+1):
#             if ((i+j)) % 2 == 0:
#                 print('1',end=" ")
#             else:
#                 print('0',end=" ")
#         print()
# binary(5)

#Just a clever math trick usefull to know though 
class Solution:
    # Function to print the alternating pattern of 1's and 0's
    def pattern11(self, N):
        # Loop over the number of rows
        for i in range(N):
            # If the row index is even, start with 1
            if i % 2 == 0:
                start = 1
            else:
                start = 0

            # Loop to print alternating 1's and 0's
            for j in range(i + 1):
                print(start, end=" ")
                # Alternate between 1 and 0
                start = 1 - start

            # Move to the next line after each row
            print()

# Driver code
sol = Solution()
N = 5
sol.pattern11(N)  # Print the pattern