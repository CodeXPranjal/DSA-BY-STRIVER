import math
class Solution:
    def isPrime(self, n):
        if n == 0 or n == 1:
            return False
        else:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
                    
            return True      