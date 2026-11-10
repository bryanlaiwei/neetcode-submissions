class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ref = {}
        for i in range(0, len(position)):
            ref[position[i]] = speed[i]
        position.sort()
        times = []
        for pos in position: 
            times.append((target - pos) / ref[pos])
        l = []
        for i in range(len(times) - 1, -1, -1):
            if not l or times[i] > l[-1]:
                l.append(times[i])
        
        return len(l)
        