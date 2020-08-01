class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return True
        
        count_lower = 0
        count_upper = 0
        
        for i in range(len(word)):    
            if word[i] >= 'a' and word[i] <= 'z':
                count_lower += 1
            elif word[i] >= 'A' and word[i] <= 'Z':
                if i == 0:
                    continue
                count_upper += 1
            
            if count_upper > 0 and count_lower > 0:
                return False
        
        return True