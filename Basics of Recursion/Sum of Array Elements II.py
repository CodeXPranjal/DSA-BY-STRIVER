class Solution:
    def arraySum(self, nums):
        if len(nums) == 0:
            return 0

        return nums[0] + self.arraySum(nums[1:])