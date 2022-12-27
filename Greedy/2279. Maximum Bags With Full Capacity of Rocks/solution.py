class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        for i in range(n):
            capacity[i] -= rocks[i]

        capacity.sort()
        for i in range(n):
            if additionalRocks > 0 and capacity[i] > 0 and additionalRocks >= capacity[i]:
                additionalRocks -= capacity[i]
                capacity[i] = 0
        
        cnt = 0
        for i in range(n):
            if capacity[i] == 0:
                cnt += 1
        return cnt
        # one line
        # return Counter(capacity)[0]
