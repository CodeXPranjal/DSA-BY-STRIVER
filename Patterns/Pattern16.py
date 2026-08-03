class Solution:
    def pattern16(self, n):
        ch=65
        for i in range(n):
            for j in range(0,i+1):
                print(chr(ch),end="")
            ch+=1
            print()
