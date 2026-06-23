class Solution:
    #fx to print a tri pattern
    def pattern(self,N):
        for i in range(N):
            for j in range(i+1):
                print("* ", end=" ")
            print()

#driver code
output = Solution()
output.pattern(N=5)

