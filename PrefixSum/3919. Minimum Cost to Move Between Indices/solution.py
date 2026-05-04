class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        if n == 0:
            return []

        # Step 1: Calculate the closest index for each element
        closest = [0] * n
        closest[0] = 1
        closest[n - 1] = n - 2
        
        for i in range(1, n - 1):
            left_diff = nums[i] - nums[i - 1]
            right_diff = nums[i + 1] - nums[i]
            # Choose the adjacent index that minimizes the difference.
            # If equal, pick the smaller index (i - 1).
            if right_diff < left_diff:
                closest[i] = i + 1
            else:
                closest[i] = i - 1

        # Step 2: Build prefix cost array for moving LEFT to RIGHT
        pre_cost = [0] * n
        for i in range(1, n):
            step_cost = nums[i] - nums[i - 1]
            if closest[i - 1] == i:
                step_cost = min(step_cost, 1)
            pre_cost[i] = pre_cost[i - 1] + step_cost

        # Step 3: Build suffix cost array for moving RIGHT to LEFT
        suf_cost = [0] * n
        for i in range(n - 2, -1, -1):
            step_cost = nums[i + 1] - nums[i]
            if closest[i + 1] == i:
                step_cost = min(step_cost, 1)
            suf_cost[i] = suf_cost[i + 1] + step_cost

        # Step 4: Answer queries in O(1) time
        ans = []
        for l, r in queries:
            if l == r:
                ans.append(0)
            elif l < r:
                # Moving forward
                ans.append(pre_cost[r] - pre_cost[l])
            else:
                # Moving backward
                ans.append(suf_cost[r] - suf_cost[l])

        return ans