class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for each in tokens:
            if each == "+":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(n1 + n2)
            elif each == "*":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(n1 * n2)
            elif each == "/":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(int(n2 / n1))
            elif each == "-":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(n2 - n1)
            else:
                stk.append(int(each))
        
        return stk[0]