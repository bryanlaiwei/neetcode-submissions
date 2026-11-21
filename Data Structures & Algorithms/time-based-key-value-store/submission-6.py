class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d: self.d[key] = [(value, timestamp)]
        else: self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ""

        lst = self.d[key]
        if timestamp < lst[0][1]: return ""

        l, r = 0, len(lst) - 1
        while l < r:
            m = math.ceil((l + r) / 2)    
            if lst[m][1] > timestamp: r = m - 1
            else: l = m
   
        return lst[l][0]
        
