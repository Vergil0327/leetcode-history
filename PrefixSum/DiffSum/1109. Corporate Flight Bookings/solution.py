# https://labuladong.github.io/algo/2/20/25/
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        for i,j, seats in bookings:
            diff[i-1] += seats
            if j < n:
                diff[j] -= seats
        
        res = [diff[0]]*n
        for i in range(1, n):
            res[i] = res[i-1] + diff[i]
        return res