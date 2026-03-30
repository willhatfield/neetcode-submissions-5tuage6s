class TimeMap:

    def __init__(self):
        self.keyMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyMap:
            self.keyMap[key] = []
            
        self.keyMap[key].append([timestamp, value])
       
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyMap:
            return ""
        
        data, res = self.keyMap[key], ""
        l, r = 0, len(data) - 1

        while l <= r:
            mid = (r + l) // 2
            if data[mid][0] <= timestamp:
                res = data[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
            

