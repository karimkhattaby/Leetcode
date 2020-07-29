class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        count = 0
        
        while i < len(nums)-count:
            if nums[i] == val:
                idx = len(nums)-count-1
                nums[i], nums[idx] = nums[idx], nums[i]
                count+=1
            else:
                i+=1
        
        return len(nums)-count