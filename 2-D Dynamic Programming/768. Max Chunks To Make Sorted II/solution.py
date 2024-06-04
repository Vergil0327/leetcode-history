class Solution:

    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        arr = [-1] + arr # to 1-indexed

        # construct maxSortedIdxFromLeft
        arr2 = list(sorted([arr[i], i] for i in range(n+1)))
        MAP = defaultdict(list)
        for i, (_, originalIdx) in enumerate(arr2):
            MAP[originalIdx] = i

        maxSortedIdxFromLeft = [0]
        for i in range(1, n+1):
            maxSortedIdxFromLeft.append(max(maxSortedIdxFromLeft[-1], MAP[i]))

        dp = [0] * (n+1)
        for i in range(1, n+1):
            minIdx = inf
            for j in range(i, 0, -1):
                minIdx = min(minIdx, MAP[j])

                if maxSortedIdxFromLeft[j-1] < minIdx:
                    dp[i] = max(dp[i], dp[j-1]+1)

        return dp[n]