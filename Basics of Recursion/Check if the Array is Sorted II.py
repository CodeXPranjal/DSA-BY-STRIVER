class Solution:
    def isSorted(self, nums):
        if len(nums)<=1:
            return True

        if nums[0] > nums[1]:
            return False

        return self.isSorted(nums[1:])