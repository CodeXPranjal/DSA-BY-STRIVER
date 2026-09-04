import math
class Solution:
    def divisors(self, n):
        n1=[]
        for i in range(1,int(math.sqrt(n))+1):
            if n%i == 0:
                n1.append(i)
                if n//i!=i:
                    n1.append(n//i)
        return sorted(n1)