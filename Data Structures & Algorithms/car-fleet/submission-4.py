class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) <= 1: return len(position)

        position, speed = zip(*sorted(zip(position, speed)))
        time = []
        for i in range(0, len(position)): time.append((target - position[i]) / speed[i])

        res = [time[len(position) - 1]]
        for i in range(len(position) - 2, -1, -1):
            curFleet = res[-1]
            if time[i] > curFleet: res.append(time[i])
        
        return len(res)
