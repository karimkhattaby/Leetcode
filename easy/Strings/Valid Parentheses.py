class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        HT = {'(': ')', '[': ']', '{': '}'}
        closing = []
        
        for i in range(len(s)):
            if s[i] in HT:
                closing.append(HT[s[i]])
            else:
                if len(closing) == 0:
                    return False
                if closing[-1] != s[i]:
                    return False
                closing.pop()
        
        return True if len(closing)==0 else False