class Solution:    
    def anagramStrings(self, s, t):
        if len(s)!=len(t):
            return False
        p=sorted(s)
        r=sorted(t)

        for i in range(len(s)):
            if p[i]!=r[i]:
                return False

        
        return True
         