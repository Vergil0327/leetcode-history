class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        sameAttack = defaultdict(list)
        for atk, defen in properties:
            heapq.heappush(sameAttack[atk], -defen)

        m = len(sameAttack)
        maxH = []
        for atk, pq in sameAttack.items():
            heapq.heappush(maxH, (pq[0], atk))

        cnt = 0
        for atk, pq in sorted(sameAttack.items()):
            while maxH and maxH[0][1] <= atk:
                heapq.heappop(maxH)

            if not maxH: break
            maxDef = -maxH[0][0]

            while pq and -pq[0] >= maxDef:
                heapq.heappop(pq)
            cnt += len(pq)
        return cnt
    
# Optimization
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0], x[1]))

        cnt = 0
        maxDefUntil = -inf
        for atk, defen in properties:
            if defen < maxDefUntil:
                cnt += 1
            else:
                maxDefUntil = max(maxDefUntil, defen)
        return cnt