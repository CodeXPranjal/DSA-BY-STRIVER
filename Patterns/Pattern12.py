class Solution:
    def pattern12(self, n):
        for i in range(1, n+1):

            # Left part
            for j in range(1, i+1):
                print(j, end="")

            # Middle spaces
            for j in range(2*(n-i)):
                print(" ", end="")

            # Right part
            for j in range(i, 0, -1):
                print(j, end="")

            print()