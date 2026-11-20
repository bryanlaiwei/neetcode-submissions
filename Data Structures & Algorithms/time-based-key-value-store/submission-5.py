class TimeMap:

    def __init__(self):
        self.d = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d: self.d[key].append((value, timestamp))
        else: self.d[key] = [(value, timestamp)]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ""
        if len(self.d[key]) == 0 or timestamp < self.d[key][0][1]: return ""
        l, r = 0, len(self.d[key]) - 1

        while l < r:
            m = math.ceil((r + l) / 2)
            if self.d[key][m][1] <= timestamp: l = m
            else: r = m - 1
        
        return self.d[key][l][0]
        
