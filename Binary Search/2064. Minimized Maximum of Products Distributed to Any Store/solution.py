class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(threshold):
            needStores = 0
            for qty in quantities:
                needStores += ceil(qty/threshold)
            return needStores <= n

        # 分配的話每個store只能1種商品，最少1個，最多max(quantities)個
        # 我們可以Greedy的方式在threshold以內去分配，只要需要的store數量小於n，那麼這個threshold就是可行解，可以再往下猜
        l, r = 1, max(quantities)
        while l < r:
            mid = l + (r-l)//2
            if canDistribute(mid):
                r = mid
            else:
                l = mid+1
        return l