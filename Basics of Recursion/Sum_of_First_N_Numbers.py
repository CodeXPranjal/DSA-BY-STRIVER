class Solution:
    def NnumbersSum(self, n):
        if n == 0:
            return 0


        return n + self.NnumbersSum(n - 1)