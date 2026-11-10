class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        l = []
        for i in range(len(cars) - 1, -1, -1):
            t = (target - cars[i][0]) / cars[i][1]
            if not l or t > l[-1]:
                l.append(t)
        
        return len(l)
        