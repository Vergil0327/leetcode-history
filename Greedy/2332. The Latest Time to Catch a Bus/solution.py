class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        m, n = len(buses), len(passengers)

        cap = j = 0
        for i in range(m):
            cap = capacity # reset current capacity
            while j < n and passengers[j] <= buses[i] and cap > 0:
                cap -= 1
                j += 1

        j -= 1 # last person step into the bus

        # if still have capacity, we can just arrive on time, i.e. buses[m-1]
        if cap > 0:
            # if someone also arrive on time
            if passengers[j] == buses[m-1]:
                j -= 1
                while j >= 0 and passengers[j]+1 == passengers[j+1]:
                    j -= 1
                return passengers[j+1]-1

            return buses[m-1]

        while j-1 >= 0 and passengers[j]-1 == passengers[j-1]:
            j -= 1
        return passengers[j]-1