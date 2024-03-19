class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        n = len(nums)

        # groupify
        def getFactors(num):
            res = []
            for i in range(2, int(sqrt(num))+1):
                if num%i == 0:
                    res.append(i)
                    while num%i == 0:
                        num //= i
            if num > 1:
                res.append(num)
            return res

        groups = defaultdict(list)
        for i in range(n):
            factors = getFactors(nums[i])
            for f in factors:
                groups[f].append(i)

        # union
        parent = list(range(n))
        rank = [1]*n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return

            if rank[px] <= rank[py]:
                parent[px] = py
                rank[py] += rank[px]
            else:
                parent[py] = px
                rank[px] += rank[py]

        for arr in groups.values():
            for i in range(1, len(arr)):
                union(arr[0], arr[i])

        # check
        v2idx = {nums[i]:i for i in range(n)}
        sorted_nums = sorted(nums)

        for i in range(n):
            if find(i) != find(v2idx[sorted_nums[i]]): return False
        return True

        # or return all(find(i) ==  find(v2idx[sorted_nums[i]]) for i in range(n))