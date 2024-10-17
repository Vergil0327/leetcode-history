class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))

        pq = [[-int(d), -i] for i, d in enumerate(s)]
        heapq.heapify(pq)

        for i, d in enumerate(s):
            while pq and -pq[0][1] <= i:
                heapq.heappop(pq)
            if pq and int(d) < -pq[0][0]:
                j = -pq[0][1]
                s[i], s[j] = s[j], s[i]
                return int("".join(s))
        return num
