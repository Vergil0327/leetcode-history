class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        n = len(arrivals)
        l = r = discard = 0
        discardElem = set()
        count = Counter()

        while r < n:
            num = arrivals[r]

            while l < r and r-l+1 > w:
                if l not in discardElem:
                    count[arrivals[l]] -= 1
                l += 1

            if count[num] < m:
                count[num] += 1
            else:
                discardElem.add(r)
                discard += 1

            r += 1

        return discard