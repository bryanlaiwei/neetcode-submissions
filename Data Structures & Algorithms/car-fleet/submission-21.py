class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) <= 1: return len(position)

        cars = sorted(zip(position, speed))

        res = 1
        curFleet = (target - cars[-1][0]) / cars[-1][-1]
        for i in range(len(position) - 2, -1, -1):
            time = (target - cars[i][0]) / cars[i][1]
            if time > curFleet: 
                curFleet = time
                res += 1
        
        return res
