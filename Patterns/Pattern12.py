class Solution:
    def pattern13(self, n):
        N=1
        for i in range(n):
            for j in range(i+1):
                print(N,end=" ")
                N+=1
            
            print()
