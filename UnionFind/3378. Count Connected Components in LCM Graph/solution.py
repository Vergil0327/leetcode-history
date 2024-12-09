class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        n = len(nums)

        nums.sort()
        res = 0
        while nums and nums[-1] > threshold:
            nums.pop()
            res += 1
        
        n = len(nums)

        parent = list(range(n))
        rank = [1] * n

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

        seen = {} # {factor: first index from first nums[i] having this factor}
        for i in range(n):
            for factor in range(1, int(sqrt(nums[i]))+1):
                if nums[i]%factor == 0:
                    x, y = factor, nums[i]//factor

                    if x in seen:
                        j = seen[x]
                        if lcm(nums[i], nums[j]) <= threshold:
                            union(i, j)
                    else:
                        seen[x] = i

                    if y in seen:
                        j = seen[y]
                        if lcm(nums[i], nums[j]) <= threshold:
                            union(i, j)
                    else:
                        seen[y] = i

        groups = set(find(i) for i in range(n))
        return res + len(groups)