# 狀態轉移就是:
# 1. 跳過rods[i]不選
# 2. rods[i]選到左邊
# 3. rods[i]選到右邊
# 不管選到左邊或右邊, 最終總和就是兩邊高度的和
# 由於兩邊一樣高, 兩邊總和除以2就是單邊高度
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)

        @cache
        def dfs(i, diff):
            if i == n:
                return 0 if diff == 0 else -inf
            res = dfs(i+1, diff)
            res = max(res, dfs(i+1, diff+rods[i]) + rods[i])
            res = max(res, dfs(i+1, diff-rods[i]) + rods[i])
            return res
        twoSideHeight = dfs(0, 0)

        if twoSideHeight > 0:
            return twoSideHeight//2
        return 0