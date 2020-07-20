class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum([x for x in range(len(nums)+1)])
        for num in nums:
            total -= num
        return total