class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""

        strs.sort()
        s1=strs[0]
        s2=strs[-1]

        for i in range (min(len(s1),len(s2))):
            if s1[i]==s2[i]:
                prefix+=s1[i]
                
            else:
                break
        
        return prefix