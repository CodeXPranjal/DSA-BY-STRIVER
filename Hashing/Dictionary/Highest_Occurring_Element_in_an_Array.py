class Solution:
    def mostFrequentElement(self, nums):

        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        m = max(freq.values())

        smallest = float('inf')

        for i in freq:
            if freq[i] == m:
                smallest = min(smallest, i)



        return smallest