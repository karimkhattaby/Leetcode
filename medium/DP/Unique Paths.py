class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 2 or n < 2:
            return 1
        dp = [[0] * m] * n
        
        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]