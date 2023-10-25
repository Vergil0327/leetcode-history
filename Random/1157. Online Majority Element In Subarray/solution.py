class MajorityChecker:

    def __init__(self, arr: List[int]):
        n = len(arr)
        self.arr = arr
        self.index = defaultdict(list)
        for i in range(n):
            self.index[arr[i]].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        rounds = 100 # 實測rounds = 10也能通過
        for i in range(rounds):
            v = self.arr[random.randint(left, right)]
            indices = self.index[v]
            l = bisect.bisect_left(indices, left)
            r = bisect.bisect_right(indices, right)
            if r-l >= threshold:
                return v
        return -1
