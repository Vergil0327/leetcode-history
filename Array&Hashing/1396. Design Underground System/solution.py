class UndergroundSystem:

    def __init__(self):
        self.records = defaultdict(dict)
        self.avg = defaultdict(dict)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.records[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        t0, start = self.records[id]

        if stationName not in self.avg[start]:
            self.avg[start][stationName] = [t-t0, 1]
        else:
            duration, accu = self.avg[start][stationName]
            self.avg[start][stationName] = [duration+t-t0, accu+1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        record = self.avg[startStation][endStation]
        return record[0]/record[1] 
