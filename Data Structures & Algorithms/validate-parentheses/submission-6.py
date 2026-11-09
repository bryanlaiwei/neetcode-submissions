class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length % 2 != 0: return False
        stack = []
        ref = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for i in range(0, length):
            if s[i] not in ref:
                stack.append(s[i])
            else: 
                try:
                    if not stack.pop() == ref[s[i]]: return False
                    else: continue
                except:
                    return False
        
        if not stack: return True
        else: return False
        