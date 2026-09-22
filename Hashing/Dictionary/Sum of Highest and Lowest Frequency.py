class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        freq={}

        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        m=max(freq.values())+min(freq.values())


        return m