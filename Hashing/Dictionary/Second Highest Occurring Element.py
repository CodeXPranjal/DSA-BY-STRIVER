class Solution:
    def secondMostFrequentElement(self, nums):
        freq={}

        for num in nums:
            freq[num]=freq.get(num,0)+1

        m=max(freq.values())
        m2=0
        for i in freq:
            if freq[i]<m:
                m2=max(freq[i],m2)


        smallest=float('inf')
        
        for i in freq:
            if freq[i]==m2:
                
                smallest=min(i,smallest)


        if smallest==float('inf'):
                return -1
                  
        return smallest