class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0
        while True:
            if j >= n:
                break
            if i-j >= m:
                nums1[i] = nums2[j]
                j+=1
            elif nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j+=1
            i+=1