class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            total += (26**i)*(ord(s[-(i+1)])-64)
        return total