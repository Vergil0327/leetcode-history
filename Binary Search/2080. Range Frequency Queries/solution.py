class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.MAP = defaultdict(list)
        for i, num in enumerate(arr):
            self.MAP[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.MAP: return 0

        start = bisect_left(self.MAP[value], left)
        end = bisect_right(self.MAP[value], right)
        return end-start
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)