class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        stack = []
        ref = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c not in ref:
                stack.append(c)
            else: 
                try:
                    if stack.pop() != ref[c]: return False
                    else: continue
                except:
                    return False
        
        return not stack
        