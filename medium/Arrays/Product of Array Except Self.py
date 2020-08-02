class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        result[1] = nums[0]
        
        for i in range(2, len(nums)):
            result[i] = result[i-1]*nums[i-1]
        
        i = len(nums)-2
        total = 1
        while i > 0:
            total *= nums[i+1]
            result[i] *= total
            i-=1
        
        result[0] = nums[1] * total
        return result