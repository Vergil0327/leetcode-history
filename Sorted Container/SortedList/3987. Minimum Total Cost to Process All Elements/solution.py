from sortedcontainers import SortedList
class Solution:
    """
    想法很簡單, 放到有序容器後, 優先找出最接近當前resource進行最有效利用
    不足的話計算出需要多少次的resource補充 (可透過數學計算O(1), 取代逐步操作)

    time complexity: nlog(n)
    space complexity: n
    """
    def minimumCost(self, nums: list[int], k: int) -> int:
        sl = SortedList(nums)
        mod = 10**9 + 7
        resource = k
        cost = 0
        penalty = 1
        while sl:
            if resource < sl[0]:
                x = ceil((sl[0] - resource) / k)
                
                # brute force
                # for _ in range(x):
                #     cost += penalty
                #     cost %= mod
                #     penalty += 1
                resource += k * x
                add = (penalty + (penalty+x-1)) * x // 2
                cost = (cost + add) % mod
                penalty += x

            i = sl.bisect_right(resource) - 1
            resource -= sl[i]
            sl.pop(i)
        return cost
