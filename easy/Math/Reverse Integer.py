class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        
        flag = False
        if x < 0:
            flag = True
            x = abs(x)
        
        while x > 0:
            digit = x%10
            result *= 10
            result += x%10
            x //= 10
        
        if flag:
            result *= -1
        if result > 2147483647 or result < -2147483648:
            result = 0
        
        return result