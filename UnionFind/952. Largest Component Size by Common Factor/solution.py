class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            factors = []
            for x in range(2, int(sqrt(num))+1):
                if num%x == 0:
                    factors.append(x)
                    while num%x == 0:
                        num //= x
            if num > 1:
                factors.append(num)
            
            # edge case: num=1 => factors = []
            if factors:
                arr.append(factors)
        
        parent = list(range(100005))
        rank = [0] * 100005

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

        for factors in arr:
            x = factors[0]
            for y in factors[1:]:
                union(x, y)
            rank[find(x)] += 1
        
        return max(rank)

# more accurate space control
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        arr = []
        maxNum = nums[0]
        for num in nums:
            maxNum = max(maxNum, num)
            factors = []
            for x in range(2, int(sqrt(num))+1):
                if num%x == 0:
                    factors.append(x)
                    while num%x == 0:
                        num //= x
            if num > 1:
                factors.append(num)
            
            # edge case: num=1 => factors = []
            if factors:
                arr.append(factors)
        
        parent = list(range((maxNum+1)))
        rank = [0] * (maxNum+1)

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

        for factors in arr:
            x = factors[0]
            for y in factors[1:]:
                union(x, y)
            rank[find(x)] += 1
        
        return max(rank)