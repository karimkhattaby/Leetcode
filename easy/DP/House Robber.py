class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) < 3:
            return max(nums)
        
        dp = [None] * (len(nums))
        dp[-1] = nums[-1]
        dp[-2] = nums[-2]
        dp[-3] = dp[-1]+nums[-3]
        
        i = -4
        while i >= (-len(nums)):
            dp[i] = nums[i] + max(dp[i+2], dp[i+3])
            i-=1
        
        return max(dp[0], dp[1])