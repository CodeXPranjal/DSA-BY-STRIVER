class Solution:
    def addDigits(self, num):
        n = 0
        if num<10:
            return num
        else:
    
            while num>0:
                temp=num%10
                n+=temp
                num//=10

                
        return self.addDigits(n)