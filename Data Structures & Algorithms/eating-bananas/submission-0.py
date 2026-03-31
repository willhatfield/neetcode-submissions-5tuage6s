class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = sum(piles)
        l, r = 1, max(piles)
        

        while l <= r:
            mid = (r + l) // 2
            time = self.timeToEat(piles, mid)

            if time > h:
                l = mid + 1
            else:
                r = mid - 1
                res = min(res, mid)

        return res
    

    def timeToEat(self, piles: List[int], k: int) -> int:
        time = 0
        for p in piles:
            time += math.ceil(p / k)
        
        return time

