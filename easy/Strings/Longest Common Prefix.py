class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        common = strs[0]
        i = 1
        while i < len(strs):
            count = 0
            for j in range(len(strs[i])):
                if j >= len(common):
                    break
                if common[j] != strs[i][j]:
                    break
                else:
                    count+=1
            common = common[:count]
            if len(common) == 0:
                break
            i+=1
        return common