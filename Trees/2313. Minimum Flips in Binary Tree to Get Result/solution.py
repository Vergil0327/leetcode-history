from functools import lru_cache
from math import inf

class TreeNode:
    def __init__(self, value: int) -> None:
        self.val = value
        self.left = self.right = None

# tree dp
# 定義 dfs(root, expected)為 子樹的運算結果為expected所需要的最少操作
class Solution:
    def  minimumFlips(root: 'TreeNode', result: bool) -> int:
        OR, AND, XOR, NOT = 2, 3, 4, 5
        
        @lru_cache(None)
        def dfs(root, expected):
            if not root.left and not root.right:
                return 1 if root.val != expected else 0
            
            res = inf
            if root.val == OR:
                # 目標是1，OR的話只要左右子樹任一為1即可為1
                # 因此左右子樹取最小的
                # res = min(res, min(left, right))
                if expected == 1:
                    left = dfs(root.left, 1)
                    right = dfs(root.right, 1)
                    res = min(res, min(left, right))
                # 必須左右子樹都是0，兩邊OR的結果才會是0
                # 所以是相加
                elif expected == 0:
                    left = dfs(root.left, 0)
                    right = dfs(root.right, 0)
                    res = min(res, left+right)
            elif root.val == AND:
                # 兩數值 AND 後為1，必須兩者都是1
                if expected == 1:
                    left = dfs(root.left, 1)
                    right = dfs(root.right, 1)
                    res = min(res, left+right)
                # 兩數值 AND 後為0，兩者任一為0即可，我們取操作數最少的一個
                elif expected == 0:
                    left = dfs(root.left, 0)
                    right = dfs(root.right, 0)
                    res = min(res, min(left, right))
            elif root.val == XOR:
                # XOR 要為1，必須`左為1右為0`或`右為0左為1`
                if expected == 1:
                    choice1 = dfs(root.left, 0) + dfs(root.right, 1)
                    choice2 = dfs(root.left, 1) + dfs(root.right, 0)
                    res = min(res, min(choice1, choice2))
                # XOR 要為0，必須左右都為1或左右都為0
                # 我們選操作數最少的一個
                elif expected == 0:
                    res = min(res, dfs(root.left, 0) + dfs(root.right, 0))
                    res = min(res, dfs(root.left, 1) + dfs(root.right, 1))
            elif root.val == NOT:
                child = root.left if root.left else root.right
                if expected == 1:
                    res = min(res, dfs(child, 0))
                elif expected == 0:
                    res = min(res, dfs(child, 1))
            return res

        return dfs(root, result)
        