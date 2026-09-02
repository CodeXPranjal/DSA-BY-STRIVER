    class Solution:
    def isPalindrome(self, n):
        rev=0
        n1=n
        while(n>0):
            temp=n%10
            rev=(rev*10)+temp
            n//=10

        return n1==rev