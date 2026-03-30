class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)
        if abs(target) > total:
            return 0

        dp = [[0] * (2 * total + 1) for _ in range(n + 1)]

        dp[0][total] = 1

        for i in range(n):
            for j in range(2 * total + 1):
                if dp[i][j] != 0:
                    dp[i + 1][j + nums[i]] += dp[i][j]
                    dp[i + 1][j - nums[i]] += dp[i][j]

        return dp[n][total + target]