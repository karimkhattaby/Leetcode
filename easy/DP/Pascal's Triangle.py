class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            current_row = [1]
            for j in range(1,i):
                temp = ans[i-1][j-1] + ans[i-1][j]
                current_row.append(temp)
            current_row.append(1)
            ans.append(current_row)
        return ans