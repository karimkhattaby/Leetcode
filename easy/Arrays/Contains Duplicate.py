class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums is None:
            return False
        if len(nums) == 1:
            return False
        
        numsSet = set()
        
        for num in nums:
            if num in numsSet:
                return True
            numsSet.add(num)
        return False