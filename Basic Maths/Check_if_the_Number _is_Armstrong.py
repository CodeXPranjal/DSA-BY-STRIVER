class Solution:
    def isArmstrong(self, n):
        temp=n
        sum=0
        for i in range(n):
            temp1=n%10
            sum+=temp1**3
            n//=10

        return sum==temp