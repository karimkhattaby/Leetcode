class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if not A:
            return 0
        
        AB_count = collections.Counter(a+b for a in A for b in B)
        return sum(AB_count.get(-(c+d),0) for c in C for d in D)