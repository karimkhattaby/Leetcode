class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return None
        if len(nums) <= 1:
            return None
        
        i = 0
        visited = {}
        
        while i<len(nums):
            val = target - nums[i]
            try:
                return [visited[val], i]
            except KeyError:
                visited[nums[i]] = i
            i+=1