# inspired by this: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/discuss/2757990/Python-3-Explanation-with-pictures-DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # total height = height[i] + depth[i]
        height = defaultdict(lambda: 0)
        depth = defaultdict(lambda: 0)
        
        # we can find max tree height from the nodes whose level is same as our query (our removed node),
        # tree height = height[query] + max depth of same level node
		# sameHeight stores nodes at each level
        sameHeight = defaultdict(list) # [depth, node]
        
        def dfs(root, level):
            if root == None:
                return -1
            
            level += 1
            height[root.val] = level
            
            left = dfs(root.left, level)
            right = dfs(root.right, level)

            depth[root.val] = 1+max(left, right)
            
            maxHeap = sameHeight[height[root.val]]
            heapq.heappush(maxHeap, [-depth[root.val], root.val])
            # sameHeight[height[root.val]].append(root.val)
            
            return 1+max(left, right)
        
        dfs(root, -1)
        
        res = []
        for q in queries:
            maxHei = height[q]
            # if we only have one node at current level
            # after we removed it, total height = height[q]-1
            if len(sameHeight[height[q]]) == 1:
                res.append(maxHei-1)
                continue

			      # TLE
            # for node in sameHeight[height[q]]:
            #     if node != q:
            #         maxHei = max(maxHei, height[node] + depth[node])
            # res.append(maxHei)
            
            maxHeap = sameHeight[height[q]]
            node = maxHeap[0][1]
            if node != q:
                res.append(-maxHeap[0][0]+height[node])
            else:
                pop = heapq.heappop(maxHeap)
                node = maxHeap[0][1]
                res.append(-maxHeap[0][0]+height[node])
                heapq.heappush(maxHeap, pop) # restore maxHeap for next query
        return res