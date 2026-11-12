class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) <= 1: return len(position)

        position, speed = zip(*sorted(zip(position, speed)))
        time = []
        for i in range(0, len(position)): time.append((target - position[i]) / speed[i])

        res = 1
        curFleet = time[-1]
        for i in range(len(position) - 1, -1, -1):
            if time[i] > curFleet: 
                curFleet = time[i]
                res += 1
        
        return res
