class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n+1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        
        for j in range(n + 1):
            dp[0][j] = j

        for row in range(1, n + 1):
            for col in range(1, m + 1):
                if word1[col - 1] == word2[row - 1]:
                    dp[col][row] = dp[col - 1][row - 1]
                else:
                    dp[col][row] = 1 + min(dp[col - 1][row - 1], dp[col][row - 1], dp[col - 1][row])
        
        return dp[-1][-1]