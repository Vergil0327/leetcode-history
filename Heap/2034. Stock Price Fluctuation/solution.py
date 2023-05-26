class StockPrice:

    def __init__(self):
        self.timeline = {}
        self.t = -1
        self.maxH = []
        self.minH = []

    def update(self, timestamp: int, price: int) -> None:
        self.timeline[timestamp] = price
        self.t = max(self.t, timestamp)
        heapq.heappush(self.maxH, [-price, timestamp])
        heapq.heappush(self.minH, [price, timestamp])

    def current(self) -> int:
        return self.timeline[self.t]
        

    def maximum(self) -> int:
        pq = self.maxH
        while pq and -pq[0][0] != self.timeline[pq[0][1]]:
            _, ts = heapq.heappop(pq)
            heapq.heappush(pq, [-self.timeline[ts], ts])

        return -pq[0][0]
        

    def minimum(self) -> int:
        pq = self.minH
        while pq and pq[0][0] != self.timeline[pq[0][1]]:
            _, ts = heapq.heappop(pq)
            heapq.heappush(pq, [self.timeline[ts], ts])

        return pq[0][0]
