class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # 离终点近的在前
        fleets = 0
        cur = 0.0
        for p, s in cars:
            t = (target - p) / s
            if t > cur:
                fleets += 1
                cur = t
        return fleets
        