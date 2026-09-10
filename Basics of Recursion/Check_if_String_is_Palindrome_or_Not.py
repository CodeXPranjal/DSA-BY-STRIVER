class Solution:
    def palindromeCheck(self, s):

        def check(left, right):
            if left >= right:
                return True

            if s[left] != s[right]:
                return False

            return check(left + 1, right - 1)

        return check(0, len(s) - 1)