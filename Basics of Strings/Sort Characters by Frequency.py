class Solution:
    def frequencySort(self, s):
        l=[]
        freq={}
        
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]]=freq.get(s[i],0)+1
            
            else:
                freq[s[i]]=1

        t = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        
        for i in t:
            l.append(i[0])
            
        return l