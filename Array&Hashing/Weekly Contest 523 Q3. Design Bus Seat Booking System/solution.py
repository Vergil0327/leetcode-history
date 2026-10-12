class BusBooking:

    def __init__(self, n: int):
        self.booked = set()
        self.costs = {}
        self.total_time = 0

    def _get_adjacent_middle(self, seat: str) -> str:
        code, row = seat[0], seat[1:]
        if code == 'A':
            return 'B' + row
        elif code == 'D':
            return 'C' + row
        return ""

    def toggle(self, seat: str) -> None:
        if seat in self.booked:
            # Unbook seat: remove recorded cost
            self.booked.remove(seat)
            cost = self.costs.pop(seat)
            self.total_time -= cost
        else:
            # Book seat: calculate cost at this moment
            code = seat[0]
            if code in ('B', 'C'):
                cost = 1
            else:
                adj_middle = self._get_adjacent_middle(seat)
                if adj_middle in self.booked:
                    cost = 3
                else:
                    cost = 1
            
            self.booked.add(seat)
            self.costs[seat] = cost
            self.total_time += cost

    def getTotalTime(self) -> int:
        return self.total_time

    def getMinTime(self) -> int:
        return len(self.booked)


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()