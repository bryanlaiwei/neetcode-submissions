class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(0, len(tokens)):
            if tokens[i] == "+":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(n1 + n2)
            elif tokens[i] == "*":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(n1 * n2)
            elif tokens[i] == "/":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(int(n2 / n1))
            elif tokens[i] == "-":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(n2 - n1)
            else:
                stk.append(int(tokens[i]))
        
        return stk[0]