class Solution:
    def reverse(self, arr: list, n: int) -> None:
        left = 0
        right = n - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1