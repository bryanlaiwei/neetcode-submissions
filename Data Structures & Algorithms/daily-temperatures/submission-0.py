class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        if not stack: stack.append(0)
        i = 1
        while i < len(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                n = stack.pop()
                res[n] = i - n
            stack.append(i)
            i += 1


        return res

        