class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        a = 1
        b = 2
        
        i = 3
        while i <= n:
            c = a+b
            a,b = b,c
            i+=1
        
        return b