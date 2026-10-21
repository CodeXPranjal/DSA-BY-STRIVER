class Solution:
    def reverseArray(self, nums):
        num=[]
        if len(nums)==0:
            return num
        
        return [nums[-1]] + self.reverseArray(nums[:-1])