class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        n = len(nums)
        largest = -inf
        for key in count.keys():
            if count[key] > n//2:
                return key