class Solution:
    def arraySortedOrNot(self, arr, n):

        count=1

        for i in range(n-1):
            if arr[i]>arr[i+1]:
                count=0

        return count 