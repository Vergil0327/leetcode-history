class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        root = 0
        rootDistSum = 0
        treeSize = defaultdict(int)

        # cnt: compute subtree size for every child which also contains child itself
        # rootDistSum: answer[0], sum of distances between every other nodes for root node 0
        def dfs(node, parent, step):
            nonlocal rootDistSum
            cnt = 0
            rootDistSum += step
            for nei in graph[node]:
                if nei != parent:
                    cnt += dfs(nei, node, step+1)+1
            
            treeSize[node] = cnt+1 # childs count + node itself
            return cnt
        dfs(root, -1, 0)
        
        # re-root
        # if we re-root from node0 to node2, every node in node0 subtree needs 1 extra step,
        # and every node in node2's child subtree can reduce 1 extra step
        # f(child) = f(parent) + a - b where a is size of parent node subtree and b is size of child subtree
        #          = f(parent) + (n-subtree(child)) - subtree(child)
        #          = f(parent) + n - 2 * subtree(child)
        ans = [0] * n
        ans[root] = rootDistSum

        def reRoot(node, parent):
            for nei in graph[node]:
                if nei == parent: continue

                b = treeSize[nei]
                a = n - b
                ans[nei] = ans[node] + a - b

                reRoot(nei, node)
        reRoot(root, -1)
        return ans