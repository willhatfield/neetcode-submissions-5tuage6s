class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []

        cars = sorted(zip(position, speed), reverse=True)

        for p, s in cars:
            ttd = (target - p) / s

            if fleet and ttd <= fleet[-1]:
                continue
            else:
                fleet.append(ttd)
        
        return len(fleet)