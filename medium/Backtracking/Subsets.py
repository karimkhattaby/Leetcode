class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        result = [[]]
        
        def gen_subsets(lst, numbers):
            if not numbers and len(lst) > 0:
                result.append(lst)
            if not numbers:
                return
            gen_subsets(lst+[numbers[-1]], numbers[:-1])
            gen_subsets(lst, numbers[:-1])
        
        gen_subsets([], nums)
        return result