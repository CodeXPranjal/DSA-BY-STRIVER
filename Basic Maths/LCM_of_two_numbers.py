class Solution:
    def LCM(self, n1, n2):
        m = max(n1, n2)

        while True:
            if m % n1 == 0 and m % n2 == 0:
                return m
            m += 1