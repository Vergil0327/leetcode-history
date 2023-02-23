class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        children = defaultdict(list)
        for child, parent in enumerate(parents):
            if parent == -1: continue
            children[parent].append(child)

        n = len(parents)
        res = [1] * n

        # find node with value `1`
        node1 = -1
        for node, num in enumerate(nums):
            if num == 1:
                node1 = node
                break
        if node1 == -1: return res
        
        node = node1
        res[node] = 0
        while parents[node] != -1:
            res[node] = 0
            node = parents[node]
        res[node] = 0
        
        has = set()
        def dfs(node, prev):
            if nums[node] in has: return

            has.add(nums[node])
            for nei in children[node]:
                if nei == prev: continue
                dfs(nei, node)

        node = node1
        missing = 1
        while node != -1:
            dfs(node, node) # add subtree to hashset

            while missing in has:
                missing += 1
            res[node] = missing

            node = parents[node]
        return res

class Solution_TLE:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        children = defaultdict(list)
        for child, parent in enumerate(parents):
            if parent == -1: continue
            children[parent].append(child)

        n = len(parents)
        res = [1] * n
        
        def dfs(node, prev):
            curr = {nums[node]}
            smallestMissing = 1
            for nei in children[node]:
                if nei == prev: continue
                smallestMissing = max(smallestMissing, res[nei])
                SET = dfs(nei, node)
                curr |= SET

            for i in range(smallestMissing, int(1e5)+1):
                if i in curr: continue
                res[node] = i
                break

            return curr
        dfs(0, 0)
        return res