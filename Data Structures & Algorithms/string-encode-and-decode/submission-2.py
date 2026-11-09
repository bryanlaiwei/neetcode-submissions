class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""
        resLst = []

        for s in strs:
            resLst.append(str(len(s)))
            resLst.append("#")
            resLst.append(s)
        
        return "".join(resLst)

    def decode(self, s: str) -> List[str]:
        res = []
        if not s: return res

        i = 0
        while i < len(s):
            j = i
            while (s[j] != "#"):
                j += 1
            length = int(s[i:j])
            singleStr = s[j + 1: j + 1 + length]
            res.append(singleStr)
            j += (1 + length)
            i = j
        
        return res

            

