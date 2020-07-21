class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)[2:]
        count = 0
        for c in s:
            if c == '1':
                count+=1
        return count