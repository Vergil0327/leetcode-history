class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Pair each number with its index and sort by value for efficient range processing
        values = [(val, idx) for idx, val in enumerate(nums)]
        values.sort()

        # Map original indices to their position in the sorted array
        index = {}
        for sorted_idx, (_, i) in enumerate(values):
            index[i] = sorted_idx

        # For each position in sorted list, determine the farthest position we can jump to
        # while still satisfying the |nums[i] - nums[j]| <= maxDiff condition
        next_pos = {}
        for idx, (val, _) in enumerate(values):
            # Use bisect to find upper bound where val + maxDiff is still valid
            pos = bisect.bisect_right(values, val + maxDiff, key=lambda x: x[0]) - 1
            next_pos[idx] = pos

        # Memoized DFS to count steps from position u to v in the sorted list
        @lru_cache(None)
        def dfs(u, v):
            if u >= v:
                return 0  # Reached or passed target

            if next_pos[u] == u:
                return -inf  # No valid move, stuck

            return 1 + dfs(next_pos[u], v)  # Move forward and count step

        ans = []
        for a, b in queries:
            u, v = index[a], index[b]
            if u > v:
                u, v = v, u  # Always go from left to right based on sorted index
            res = dfs(u, v)
            ans.append(res if res > -inf else -1)  # -1 means path not possible

        return ans
