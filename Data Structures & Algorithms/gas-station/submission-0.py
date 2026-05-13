class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Input: gas = [1,2,3,4], 
        # cost =       [2,2,4,1]
        # 
        
        if sum(gas) < sum(cost):
            return -1

        res, total = 0, 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = (i + 1) % len(gas)
        
        return res