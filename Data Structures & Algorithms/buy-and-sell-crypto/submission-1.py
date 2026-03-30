class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l, r = 0, 0
        while(r < len(prices)):
            currProf = prices[r] - prices[l]
            if currProf < 0:
                l = r

            maxProf = max(maxProf, currProf)

            r = r + 1 
        return maxProf