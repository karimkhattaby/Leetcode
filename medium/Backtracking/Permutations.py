class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        
        permutations = []
        
        for i in range(len(nums)):
            for lst in self.permute(nums[:i]+nums[i+1:]):
                permutations.append([nums[i]]+lst)
        
        return permutations