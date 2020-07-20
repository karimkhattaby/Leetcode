class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for idx, letter in enumerate(s):
            if count[letter] == 1:
                return idx
        return -1