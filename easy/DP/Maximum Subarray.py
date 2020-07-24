class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [None] * len(nums)
        dp[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            dp[i] = max(nums[i], nums[i]+dp[i+1])
        return max(dp)