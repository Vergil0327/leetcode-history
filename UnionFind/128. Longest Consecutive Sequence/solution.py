# Union-Find
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {}
        rank = {}
        S = set(nums)

        def find(x):
            if x not in parent: return None
            
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px is None or py is None: return
            if px == py: return
            
            if rank[py] >= rank[px]:
                rank[py] += rank[px]
                parent[px] = py
            else:
                rank[px] += rank[py]
                parent[py] = px
        
        for num in S:
            parent[num] = num
            rank[num] = 1
            
            if num-1 in S:
                union(num-1, num)
            if num+1 in S:
                union(num+1, num)
                
        return max(rank.values(), default=0)