class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) <= 1: return len(position)

        position, speed = zip(*sorted(zip(position, speed)))

        res = 1
        curFleet = (target - position[-1]) / speed[-1]
        for i in range(len(position) - 2, -1, -1):
            time = (target - position[i]) / speed[i]
            if time > curFleet: 
                curFleet = time
                res += 1
        
        return res
