class Solution:
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1,-1][x<0]
        rev = 0
        x = abs(x)
        while x:
            x, mod = divmod(x,10)
            rev = rev*10 + mod
            
        return rev*sign if -pow(2,31) <= rev * sign <= pow(2,31)-1 else 0
    
        