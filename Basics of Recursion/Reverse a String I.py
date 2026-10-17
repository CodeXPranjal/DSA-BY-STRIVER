class Solution:
    def reverseString(self, s):
        if len(s) == 0:
            return []

        return [s[-1]] + self.reverseString(s[:-1])