class Solution:
    def pattern18(self, n):
        ch = 65
        for i in range(1,n+1):
            for j in range(i,0,-1):
                print(chr(ch+n-j),end=" ")

            print()
            
        