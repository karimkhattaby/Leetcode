class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        s = s.split()
        for k in range(len(s)):
            if not s[k]:
                continue
            word = list(s[k])
            for i in range(len(word)//2):
                word[i], word[-(i+1)] = word[-(i+1)], word[i]
            s[k] = ''.join(word)
        return ' '.join(s)