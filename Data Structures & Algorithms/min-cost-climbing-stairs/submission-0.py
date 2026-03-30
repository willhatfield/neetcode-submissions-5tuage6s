class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        arr = [0] * (n + 1)

        start = 2

        for i in range(start, n + 1):
            arr[i] = min(cost[i - 1] + arr[i - 1], cost[i - 2] + arr[i - 2])

        return arr[-1]