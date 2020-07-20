class Solution:
    def isHappy(self, n: int) -> bool:
        HT = {}
        while n > 1:
            nums = []
            HT[n] = True
            while n > 0:
                nums.append(n%10)
                n = n//10
            for i in range(len(nums)):
                n += (nums[i]**2)
            if n in HT:
                return False
        return True if n==1 else False