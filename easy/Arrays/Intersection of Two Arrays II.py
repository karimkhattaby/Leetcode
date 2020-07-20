class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)
        ans = count1 & count2
        return [key for key in ans for _ in range(ans[key])]