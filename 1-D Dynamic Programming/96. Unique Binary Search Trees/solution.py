# time: O(n^2)
# space: O(n)
class TopDownSolution:
    @functools.lru_cache(None)
    def numTrees(self, n: int) -> int:
        if n < 2: return 1

        cnt = 0
        # [1,2,3,4,...,n-1,n], consider each of value as root node
        # 1 as root, numTrees(0) as left subtree and numTrees(n-1) as right subtree
        # 2 as root, numTrees(1) as left subtree and numTrees(n-2) as right subtree
        for i in range(n):
            # cnt += combinations of left subtree * combinations of right subtree
            cnt += self.numTrees(i) * self.numTrees(n-i-1)
        return cnt

class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] : how many possible BST if we use i nodes
        dp = [0] * (n+1)
        dp[0] = 1 # how many possible BST if we use zero node ? ans = 1, use one None
        dp[1] = 1 # how many possible BST if we use one node ? ans = 1: one root node
        
        # n nodes, we start from 2 nodes since we've already compute dp[0] & dp[1] as base case
        for nodes in range(2, n+1):
            # choose 1...n as root node
            for root in range(1, nodes+1):
                left = dp[root-1]
                right = dp[nodes-root]
                dp[nodes] += left * right
        return dp[n]