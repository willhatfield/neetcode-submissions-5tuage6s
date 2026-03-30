class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []

        cars = sorted(zip(position, speed), reverse=True)

        lastSlow = 0
        count = 0
        for p, s in cars:
            ttd = (target - p) / s

            if ttd <= lastSlow:
                continue
            else:
                lastSlow = ttd
                count += 1
        
        return count