from sortedcontainers import SortedList

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.map[key])-1
        
        if not self.map[key]: return ""
        
        if self.map[key][l][0] > timestamp:
            return ""
        if self.map[key][r][0] <= timestamp:
            return self.map[key][r][1]
        
        
        while l < r:
            mid = r - (r-l)//2
            if self.map[key][mid][0] <= timestamp:
                l = mid
            else:
                r = mid-1

        ts, val = self.map[key][l]
        if ts <= timestamp:
            return val
        else:
            return ""

class TimeMapSortedList:

    def __init__(self):
        self.map = defaultdict(SortedList)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.map[key])-1
        
        if not self.map[key]: return ""

        idx = self.map[key].bisect_left((timestamp, ""))
        
        if idx == len(self.map[key]):
            if idx > 0 and self.map[key][idx-1][0] <= timestamp:
                return self.map[key][idx-1][1]
            else:
                return ""
        
        ts, val = self.map[key][idx]
        if ts <= timestamp:
            return val
        elif idx > 0 and self.map[key][idx-1][0] <= timestamp:
            return self.map[key][idx-1][1]
        else:
            return ""

class TimeMapSortedListOptimized:

    def __init__(self):
        self.map = defaultdict(SortedList)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.map[key])-1
        
        if not self.map[key]: return ""
        
        if self.map[key][l][0] > timestamp:
            return ""
        if self.map[key][r][0] <= timestamp:
            return self.map[key][r][1]

        idx = self.map[key].bisect_left((timestamp, ""))
        
        ts, val = self.map[key][idx]
        if ts <= timestamp:
            return val
        else:
            return self.map[key][idx-1][1]

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect_right(self.map[key], [timestamp], key= lambda arr: [arr[0]])

        if idx > 0 and self.map[key][idx-1][0] <= timestamp:
            return self.map[key][idx-1][1]
        else:
            return ""
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)