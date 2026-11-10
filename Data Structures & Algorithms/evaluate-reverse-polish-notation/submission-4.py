class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tk in tokens:
            if tk == "+":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 + n2)
            elif tk == "-":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 - n2)
            elif tk == "*":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 * n2)
            elif tk == "/":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(int(n1 / n2))
            else:
                stack.append(int(tk))

        return stack[0]
        