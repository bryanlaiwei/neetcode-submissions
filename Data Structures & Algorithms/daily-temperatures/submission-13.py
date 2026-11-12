class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(0, len(temperatures)):
            if not stack or temperatures[i] < temperatures[stack[-1]]: 
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    idx = stack.pop()
                    res[idx] = i - idx
                stack.append(i)
                    
        return res