from sortedcontainers import SortedList

class RideSharingSystem:
    """
    int[] matchDriverWithRider() Matches the earliest available driver with the earliest waiting rider and removes both of them from the system. Returns an integer array of size 2 where result = [driverId, riderId] if a match is made. If no match is available, returns [-1, -1].
    void cancelRider(int riderId) Cancels the ride request of the rider with the given riderId if the rider exists and has not yet been matched.
    """

    def __init__(self):
        self.t = 0
        self.riders = SortedList()
        self.drivers = SortedList()
        self.riderIdx = {}
        self.driverIdx = {}

    def addRider(self, riderId: int) -> None:
        self.riderIdx[riderId] = self.t
        self.riders.add([self.t, riderId])
        self.t += 1
        

    def addDriver(self, driverId: int) -> None:
        self.driverIdx[driverId] = self.t
        self.drivers.add([self.t, driverId])
        self.t += 1
        

    def matchDriverWithRider(self) -> List[int]:
        if (self.riders and self.drivers):
            driverId = self.drivers[0][1]
            riderId = self.riders[0][1]
            ans = [driverId, riderId]
            self.riders.pop(0)
            self.drivers.pop(0)
            del self.driverIdx[driverId]
            del self.riderIdx[riderId]
            return ans
        else:
            return [-1, -1]
        

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riderIdx:
            t = self.riderIdx[riderId]
            del self.riderIdx[riderId]
            self.riders.remove([t, riderId])
        


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)