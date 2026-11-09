class Solution:
    def calPoints(self, operations: List[str]) -> int:
        resLst = []
        res = 0
        for op in operations:
            if op == "+":
                resLst.append(resLst[-1] + resLst[-2])
                res += (resLst[-2] + resLst[-3])
            elif op == "D":
                resLst.append(resLst[-1] * 2)
                res += resLst[-1]
            elif op == "C":
                res -= resLst.pop()
            else:
                resLst.append(int(op))
                res += int(op)
        
        return res
        