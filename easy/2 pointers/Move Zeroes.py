class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        if len(nums) < 2:
            return nums
        zero_pointer, pointer = 0, 1
        while pointer < len(nums):
            if nums[zero_pointer] != 0:
                zero_pointer+=1
            elif nums[zero_pointer] == 0 and nums[pointer] != 0:
                nums[pointer], nums[zero_pointer] = nums[zero_pointer], nums[pointer]
                zero_pointer+=1
            pointer+=1