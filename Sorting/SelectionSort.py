class Solution:
    def selectionSort(self, nums):
        n=len(nums)
        for i in range(0,n-1):

            smallest=i

            for j in range(i+1,n):
                if nums[j]<nums[smallest]:
                    smallest=j

            nums[i],nums[smallest]=nums[smallest],nums[i]


        return nums