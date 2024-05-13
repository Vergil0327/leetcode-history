class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        cost2 = min(cost1*2, cost2)

        n = len(nums)
        nums.sort()

        total = sum(nums)
        res = inf
        # target 為最終equal的數量
        for target in range(nums[-1], nums[-1]*2 + 1):
            step0 = target - nums[0]
            tot_step = n * target - total

            if step0 > tot_step//2:
                num_cost2 = (tot_step - step0)
                cost = num_cost2 * cost2 + (step0 - num_cost2) * cost1

            else: # 全部配對成 cost2 op., 僅留下最終一個烙單的數 => 看tot_step是奇數或偶數
                cost = (tot_step//2) * cost2 + (cost1 if tot_step%2 == 1 else 0)

            if cost < res:
                res = cost
            elif cost > res:
                # 最後這段代表的意義是:
                # 我們在拉高target = max(nums) + X時
                # 目的是在將cost1 op.替換成cost2 op.來降低整體cost
                # 但如果我們已經到了最佳值之後, 仍繼續往上搜索target的話
                # 相當於我們多了許多多餘的cost2 op., 想了一下會發現這可能是個開口向上的曲線
                # 我們將cost1 op. 配對成cost2 op.時, 會逐漸降低cost 值到一個最佳點
                # 但如果之後我們繼續在拉高上限, 配出更多cost2 op.的話, cost就又會上升了
                # 所以我們僅需要將target拉高到最低cost即可
                break

        return res % 1_000_000_007
