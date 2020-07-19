class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ''' SOLUTION 1, O(n) time, O(n) space
        count = collections.Counter(nums)
        for item in count:
            if count[item] == 1:
                return item'''
        '''SOLUTION 2, O(n) time, O(1) space'''
        answer = 0
        
        for num in nums:
            answer ^= num
            
        return answer