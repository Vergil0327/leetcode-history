MX = 50001
divisors = [[] for _ in range(MX)]
for x in range(1, MX):
    for y in range(x, MX, x):
        divisors[y].append(x)

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        countNum = Counter(nums)
        countD = Counter()  # countD[d]: number of (i) with nums[i] % d == 0
        for num, freq in countNum.items():
            for d in divisors[num]:
                countD[d] += freq

        countG = Counter()  # countG[g]: number of (i < j) with gcd(nums[i], nums[j]) == g
        for g in range(mx, 0, -1):
            c = countD[g]
            if c <= 1:
                continue
            countG[g] = c * (c - 1) // 2
            countG[g] -= sum(countG[x] for x in range(2 * g, mx + 1, g))
        
        gList = []
        vList = []
        for g, v in sorted(countG.items()):
            gList.append(g)
            vList.append(v)
        presumV = list(accumulate(vList))

        res = []
        for q in queries:
            i = bisect_right(presumV, q)
            res.append(gList[i])
        return res