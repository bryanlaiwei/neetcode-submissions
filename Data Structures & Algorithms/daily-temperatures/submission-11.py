class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        idxStack = []

        for i in range(0, len(temperatures)):
            if not stack or temperatures[i] < stack[-1]: 
                stack.append(temperatures[i])
                idxStack.append(i)
            else:
                while stack and temperatures[i] > stack[-1]:
                    stack.pop()
                    idx = idxStack.pop()
                    res[idx] = i - idx
                stack.append(temperatures[i])
                idxStack.append(i)
                    
        return res