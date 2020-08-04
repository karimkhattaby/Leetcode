class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        i = 0
        while 4**i <= num:
            if 4**i == num:
                return True
            i+=1
        return False