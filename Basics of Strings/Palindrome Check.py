class Solution:    
    def palindromeCheck(self, s):

        n=len(s)
        s1=''
        for i in range(n-1,-1,-1):
            s1+=s[i]
        
        return s==s1

        