class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda x:-x[0]) # sort by profit in decreasing order
        
        res = totalProfit = 0
        distinct = defaultdict(int)
        duplicate = []
        for i in range(k):
            totalProfit += items[i][0]
            if items[i][1] in distinct:
                duplicate.append(items[i][0])
            distinct[items[i][1]] += 1

        res = totalProfit + pow(len(distinct), 2)

        for i in range(k, len(items)):
            if not duplicate: break
            if items[i][1] in distinct: continue
            distinct[items[i][1]] += 1
            totalProfit += items[i][0] - duplicate.pop()
            res = max(res, totalProfit + pow(len(distinct), 2))
        return res
