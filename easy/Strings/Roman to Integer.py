class Solution:
    def romanToInt(self, s: str) -> int:
        HT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        s = s.upper()
        for i in range(len(s)):
            if i+1 == len(s):
                total += HT[s[i]]
                break
            elif HT[s[i]] < HT[s[i+1]]:
                total -= HT[s[i]]
            else:
                total += HT[s[i]]
        return total